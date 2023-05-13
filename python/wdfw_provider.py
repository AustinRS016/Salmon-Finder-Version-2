import os

from typing import Any

from dotenv import load_dotenv
from sodapy import Socrata
import pandas as pd

from hatchery_provider_meta import HatcheryProviderLogic, HatcheryProviderResponse

# TODO move this to entry point 
load_dotenv()


class WDFWProviderLogic(HatcheryProviderLogic):
    def get_hatchery_data(self, hatchery_name, date=None) -> HatcheryProviderResponse:
        """
        Example inputs:
        Parameters:
            hatchery: string
                The name of the hatchery from the config
            date: string
                Optional parameter to query from a specific date
                Format: YYYY-MM-DD
        Returns:
            hatcheryData: list of dictionaries for each row in dataset
        """

        date_query = f"AND date > '{date}'" if date is not None else ""

        client = Socrata(
            "data.wa.gov",
            os.getenv("APP_KEY"),
            username=os.getenv("APP_USERNAME"),
            password=os.getenv("APP_PASSWORD"),
        )

        # Limit defaults to 1000, not sure what to put for 'no-limit' dataset is ~450,000 rows
        #  use limit=1 for testing purposes and limit=10000000 for development
        results = client.get(
            "9q4e-xhag",
            limit=100000000,
            select="species, origin, run, facility, adult_count, date",
            where=f"""
                facility='{hatchery_name}'
                AND event='Trap Estimate'
                AND adult_count > 0
                {date_query}
                AND (
                    species='Coho'
                    OR species='Chinook'
                    OR species='Steelhead'
                    OR species='Chum'
                    OR species='Pink'
                    OR species='Sockeye'
                )""",
        )
        df = self._WDFW_to_df(results)
        distinct_populations = self._find_distinct_populations(df)
        return HatcheryProviderResponse(distinct_populations, df)
    
    def _find_distinct_populations(self, df) -> list[dict[str, str]]:
        """
        Parameters:
            df: pandas dataframe of data returned from getWDFWData
        Output: 
            distinct_populations: List of dictionaries
                example: [{'species': 'Chinook', 'origin': 'WILD', run: 'Summer'}]
        """
        # Group by species -> run -> origin
        species = df.species.unique()

        distinctPopulations = []

        for s in species:
            df_s = df[df.species == s]
            run = df_s.run.unique()
            for r in run:
                df_r = df_s[df_s.run == r]
                origin = df_r.origin.unique()
                for o in origin:
                    distinctPopulations.append(
                        {'species': s, 'run': r, 'origin': o,})              
        return distinctPopulations

    def _WDFW_to_df(self, results):

        '''
        Paramters:
            results: list of dictionaries for each row in the dataset
        Outputs:
            df: pandas dataframe representing 
        '''
        df = pd.DataFrame(results)
        df.drop_duplicates()
        df['date'] = pd.to_datetime(df['date'])
        df['adult_count'] = pd.to_numeric(df['adult_count'])
        df['DOY'] = df['date'].dt.strftime('%j')
        df['Year'] = df['date'].dt.strftime('%Y')
        return df

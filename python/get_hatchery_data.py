import os

from typing import Any

from dotenv import load_dotenv
from sodapy import Socrata
import pandas as pd

from hatchery_provider_meta import HatcheryProviderLogic

load_dotenv()


class WDFWProviderLogic(HatcheryProviderLogic):
    def get_fish_data(self, hatchery, date=None) -> Any:
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
                facility='{hatchery}'
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
        print(results)
        # df = WDFW_to_df(results)
        return results


# def get_WDFW_Data(hatchery, date=""):
#     """
#     Example inputs:    
#     Parameters: 
#         hatchery: string
#             The name of the hatchery from the config
#         date: string
#             Optional parameter to query from a specific date
#             Format: YYYY-MM-DD
#     Returns:
#         hatcheryData: list of dictionaries for each row in dataset
#     """
#     if (date != ""):
#         date_query = f"AND date > '{date}'"
#     else:
#         date_query = ""

#     client = Socrata("data.wa.gov",
#                      os.getenv('APP_KEY'),
#                      username=os.getenv('APP_USERNAME'),
#                      password=os.getenv('APP_PASSWORD'))

#     # Limit defaults to 1000, not sure what to put for 'no-limit' dataset is ~450,000 rows
#     #  use limit=1 for testing purposes and limit=10000000 for development
#     results = client.get("9q4e-xhag", limit=1000000000, select="species, origin, run, facility, adult_count, date",
#                          where=f"""
#                         facility='{hatchery}' 
#                         AND event='Trap Estimate'
#                         AND adult_count > 0 
#                         {date_query}
#                         AND (
#                             species='Coho'
#                             OR species='Chinook' 
#                             OR species='Steelhead'
#                             OR species='Chum' 
#                             OR species='Pink' 
#                             OR species='Sockeye' 
#                             )"""
#                          )
#     return results

def WDFW_to_df(results):

    '''
    Paramters:
        results: list of dictionaries for each row in the dataset
    Outputs:
        df: pandas dataframe
    '''
    df = pd.DataFrame(results)
    print(df)
    df.drop_duplicates()
    df['date'] = pd.to_datetime(df['date'])
    df['adult_count'] = pd.to_numeric(df['adult_count'])
    df['DOY'] = df['date'].dt.strftime('%j')
    df['Year'] = df['date'].dt.strftime('%Y')
    return df

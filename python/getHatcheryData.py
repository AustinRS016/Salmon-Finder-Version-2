import pandas as pd
from sodapy import Socrata
import os
from dotenv import load_dotenv

load_dotenv()


def getWDFWData(hatchery, date=""):
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
    if (date != ""):
        dateQuery = f"AND date > '{date}'"
    else:
        dateQuery = ""

    client = Socrata("data.wa.gov",
                     os.getenv('APP_KEY'),
                     username=os.getenv('APP_USERNAME'),
                     password=os.getenv('APP_PASSWORD'))

    # Limit defaults to 1000, not sure what to put for 'no-limit' dataset is ~450,000 rows
    #  use limit=1 for testing purposes and limit=10000000 for development
    results = client.get("9q4e-xhag", limit=100, select="species, origin, run, facility, adult_count, date",
                         where=f"""
                        facility='{hatchery}' 
                        AND event='Trap Estimate'
                        AND adult_count > 0 
                        {dateQuery}
                        AND (
                            species='Coho'
                            OR species='Chinook' 
                            OR species='Steelhead'
                            OR species='Chum' 
                            OR species='Pink' 
                            OR species='Sockeye' 
                            )"""
                         )
    return results


prin

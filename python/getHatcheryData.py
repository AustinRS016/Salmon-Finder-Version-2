import pandas as pd
from sodapy import Socrata
import os
from dotenv import load_dotenv
from filterHatcheryData import *

load_dotenv()

client = Socrata("data.wa.gov",
                 os.getenv('APP_KEY'),
                 username= os.getenv('APP_USERNAME'),
                 password= os.getenv('APP_PASSWORD'))

# Limit defaults to 1000, not sure what to put for 'no-limit' dataset is ~450,000 rows
#  use limit=1 for testing purposes and limit=10000000 for development
results = client.get("9q4e-xhag", limit=1000)

results_df = pd.DataFrame.from_records(results)

# Save this data to our DB
final_df = filterHatcheryData(results_df)

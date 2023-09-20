from dotenv import load_dotenv

from ....main.config.config import hatcheries
from create_graph_data import (
    compute_bargraph_data,
    get_rolling_average,
    get_recent_escapement,
)

hatchery_name = "COWLITZ SALMON HATCHERY"
provider = hatcheries[hatchery_name].provider

hatchery_provider_response = provider.hatchery_provider.value.get_hatchery_data(
    hatchery_name
)

# recent_escapement = get_recent_escapement(hatchery_provider_response)

# with open (f"{hatchery_name}_recent_escapement.json", "w") as outfile:
#     outfile.write(recent_escapement)


# Outputs as JSON
# bargraph = compute_bargraph_data(hatchery_provider_response)
# rolling_average = get_rolling_average(hatchery_provider_response)


# '''
# This is how I created my local dev data
# '''
# with open (f"{hatchery_name}_bargraph.json", "w") as outfile:
#     outfile.write(bargraph)

# with open(f"{hatchery_name}_areagraph.json", "w") as outfile:
#     outfile.write(rolling_average)

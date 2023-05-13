from config import hatcheries
from wdfw_provider import WDFWProviderLogic
from create_graph_data import compute_bargraph_data, get_rolling_average

wdfw_provider_logic = WDFWProviderLogic()

for hatchery_name, provider in hatcheries.items():

    hatchery_provider_response = provider.hatchery_provider.value.get_hatchery_data(hatchery_name)

    # Outputs as JSON
    bargraph = compute_bargraph_data(hatchery_provider_response)
    rolling_average = get_rolling_average(hatchery_provider_response)

    '''
    This is how I created my local dev data
    '''
    with open (f"{hatchery_name}_bargraph.json", "w") as outfile:
        outfile.write(bargraph)

    with open (f"{hatchery_name}_areagraph.json", "w") as outfile:
        outfile.write(rolling_average)

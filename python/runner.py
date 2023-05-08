from config import hatcheries
from get_hatchery_data import WDFWProviderLogic
from create_graph_data import compute_bargraph_data, get_rolling_average

wdfw_provider_logic = WDFWProviderLogic()

for hatchery_name, provider in hatcheries.items():

    df = provider.hatchery_provider.value.get_fish_data(hatchery_name)

    distinct_populations = provider.hatchery_provider.value.find_distinct_populations(df)

    # Outputs as JSON
    bargraph = compute_bargraph_data(df, distinct_populations)
    rolling_average = get_rolling_average(df, distinct_populations)

    '''
    This is how I created my local dev data
    '''
    with open (f"{hatchery_name}_bargraph.json", "w") as outfile:
        outfile.write(bargraph)

    with open (f"{hatchery_name}_areagraph.json", "w") as outfile:
        outfile.write(rolling_average)

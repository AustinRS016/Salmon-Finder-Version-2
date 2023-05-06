from config import hatcheries
from get_hatchery_data import WDFWProviderLogic, WDFW_to_df
from create_graph_data import find_distinct_populations, compute_bargraph_data, get_rolling_average

wdfw_provider_logic = WDFWProviderLogic()

print(wdfw_provider_logic)
x = 0
for hatchery_name, provider in hatcheries.items():
    if x > 1:
        break
    df = provider.hatchery_provider.value.get_fish_data(hatchery_name)
    print(df)

    distinct_populations = find_distinct_populations(df)

    # Outputs as JSON
    bargraph = compute_bargraph_data(df, distinct_populations)
    rolling_average = get_rolling_average(df, distinct_populations)

    with open (f"{hatchery_name}_bargraph.json", "w") as outfile:
        outfile.write(bargraph)

    with open (f"{hatchery_name}_areagraph.json", "w") as outfile:
        outfile.write(rolling_average)
    x = x + 1

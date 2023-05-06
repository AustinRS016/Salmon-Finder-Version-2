from get_hatchery_data import get_WDFW_Data, WDFW_to_df
from create_graph_data import find_distinct_populations, compute_bargraph_data, get_rolling_average
from data import testData

data = get_WDFW_Data('WALLACE R HATCHERY')
df = WDFW_to_df(data)

distinct_populations = find_distinct_populations(df)

bargraph = compute_bargraph_data(df, distinct_populations)

rolling_average = get_rolling_average(df, distinct_populations)

with open ("bargraph.json", "w") as outfile:
    outfile.write(bargraph)

with open ("rolling_average.json", "w") as outfile:
    outfile.write(rolling_average)
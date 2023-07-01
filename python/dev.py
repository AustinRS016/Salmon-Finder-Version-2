from dotenv import load_dotenv

from config import hatcheries
from create_graph_data import (
    compute_bargraph_data,
    compute_KDE,
    get_recent_escapement)

# hatchery_name = "COWLITZ SALMON HATCHERY"
# provider = hatcheries[hatchery_name]

# hatchery_provider_response = provider.hatchery_provider.value.get_hatchery_data(
#     hatchery_name
# )


for hatchery_name, provider in hatcheries.items():
    hatchery_provider_response = provider.hatchery_provider.value.get_hatchery_data(
        hatchery_name
    )

    # Outputs as JSON
    bargraph = compute_bargraph_data(hatchery_provider_response)
    density_estimation = compute_KDE(hatchery_provider_response)
    recent_escapement = get_recent_escapement(hatchery_provider_response)

    with open(f"{hatchery_name}bargraph.json", "w") as outfile:
        outfile.write(bargraph)

    with open(f"{hatchery_name}areagraph.json", "w") as outfile:
        outfile.write(density_estimation)

    with open(f"{hatchery_name}recent_escapement.json", "w") as outfile:
        outfile.write(recent_escapement)

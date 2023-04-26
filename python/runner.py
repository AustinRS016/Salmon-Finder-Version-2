from config import hatcheries, HatcheryProvider
from get_hatchery_data import get_wdfw_data

for hatchery_name, provider in hatcheries.items():
    if provider.hatchery_provider is HatcheryProvider.WA_HATCHERY_DATA:
        data = get_wdfw_data(hatchery_name)
        print(data)

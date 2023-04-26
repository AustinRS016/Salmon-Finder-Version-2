from config import hatcheries, HatcheryProvider
from get_hatchery_data import WDFWProviderLogic

wdfw_provider_logic = WDFWProviderLogic()

for hatchery_name, provider in hatcheries.items():
    if provider.hatchery_provider is HatcheryProvider.WA_HATCHERY_DATA:
        data = wdfw_provider_logic.get_fish_data(hatchery_name)
        print(data)

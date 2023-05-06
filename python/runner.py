from config import hatcheries
from get_hatchery_data import WDFWProviderLogic

wdfw_provider_logic = WDFWProviderLogic()

for hatchery_name, provider in hatcheries.items():
    data = provider.hatchery_provider.value.get_fish_data(hatchery_name)
    print(data)

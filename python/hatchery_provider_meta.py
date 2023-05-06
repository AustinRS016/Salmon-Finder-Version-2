from abc import ABC, abstractmethod
from typing import Any


class HatcheryProviderLogic(ABC):
    #poop
    @abstractmethod
    def get_fish_data(self, hatchery, date=None) -> Any:
        pass
    def find_disctinct_populations(self, df) -> Any:
        pass

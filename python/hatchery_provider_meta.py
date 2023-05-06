from abc import ABC, abstractmethod
from typing import Any


class HatcheryProviderLogic(ABC):
    @abstractmethod
    def get_fish_data(self, hatchery, date=None) -> Any:
        pass

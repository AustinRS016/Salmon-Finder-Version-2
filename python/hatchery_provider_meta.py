import pandas as pd

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class HatcheryProviderResponse:
    """
    df: pandas dataframe with columns:
                ['species', 'origin', 'run', 'facility', 'adult_count', 'date', 'DOY', 'Year']
    distinct_population: List of dictionaries
            example: [{'species': 'Chinook', 'origin': 'WILD', run: 'Summer'}]
    """

    distinct_populations: list[dict[str, str]]
    df: pd.DataFrame


class HatcheryProviderLogic(ABC):
    @abstractmethod
    def get_hatchery_data(self, hatchery_name, date=None) -> HatcheryProviderResponse:
        pass

from dataclasses import dataclass
from enum import Enum, auto


class HatcheryProvider(Enum):
    WA_HATCHERY_DATA = auto()


@dataclass
class Provider:
    hatchery_provider: HatcheryProvider


hatcheries = {
    "BAKER LAKE HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "BEAVER CREEK HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "BINGHAM CREEK HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "BOGACHIEL HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "CEDAR RIVER HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "CHIWAWA HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "COTTONWOOD CREEK POND": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "COWLITZ SALMON HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "DUNGENESS HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "EASTBANK HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "ELWHA HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "FORKS CREEK HARISON HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "GEORGE ADAMS HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "HOODSPORT HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "HUMPTULIPS HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "HURD CREEK HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "ICY CREEK HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "ISSAQUAH HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "KENDALL CREEK HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "LEWIS RIVER HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "LYONS FERRY HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "MARBLEMOUNT HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "MCKERNAN HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "MINTER CREEK HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "NASELLE HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "NEMAH HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "NORTH TOUTLE HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "PRIEST RAPIDS HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "REITER PONDS": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "RINGOLD SPRINGS HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "SAMISH HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "SKAMANIA HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "SKOOKUMCHUCK HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "SOOS CREEK HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "SPEELYAI HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "TOKUL CREEK HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "TUCANNON HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "TUMWATER FALLS HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "VOIGHTS CREEK HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "WASHOUGAL HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "FOSTER RD TRAP": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "KALAMA FALLS HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "LK ABERDEEN HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "MERWIN DAM FCF": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "MODROW TRAP": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "SOLDUC HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "SUNSET FALLS FCF": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "WALLACE R HATCHERY": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "WASHOUGAL RIVER FISH WEIR": Provider(HatcheryProvider.WA_HATCHERY_DATA),
    "WHITEHORSE POND": Provider(HatcheryProvider.WA_HATCHERY_DATA),
}
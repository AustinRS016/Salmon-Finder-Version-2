from dataclasses import dataclass
from enum import Enum

from wdfw_provider import WDFWProviderLogic


class HatcheryProvider(Enum):
    WA_HATCHERY_DATA = WDFWProviderLogic()


@dataclass
class Provider:
    hatchery_provider: HatcheryProvider


@dataclass
class HatcheryConfig:
    provider: Provider
    facility: str
    wria: str
    river_gauge: str
    lat: float
    long: float


hatcheries = {
    "BAKER LAKE HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "BAKER_LK_HATCHERY",
        "UPPER SKAGIT",
        "12194000",
        -121.6981,
        48.6491,
    ),
    "BEAVER CREEK HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "BEAVER_CR_HATCHERY",
        "GRAYS-ELOKOMAN",
        "",
        -123.3287,
        46.2259,
    ),
    "BINGHAM CREEK HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "BINGHAM_CR_HATCHERY",
        "LOWER CHEHALIS",
        "12035000",
        -123.4003,
        47.1461,
    ),
    "BOGACHIEL HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "BOGACHIEL_HATCHERY",
        "SOLEDUCK-HOH",
        "12042800",
        -124.4389,
        47.9349,
    ),
    "CEDAR RIVER HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "CEDAR_RIVER_HATCHERY",
        "CEDAR-SAMMAMISH",
        "12117500",
        -121.9625,
        47.3761,
    ),
    "CHIWAWA HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "CHIWAWA_HATCHERY",
        "WENATCHEE",
        "12459000",
        -120.6519,
        47.789,
    ),
    "COTTONWOOD CREEK POND": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "COTTONWOOD_CR_POND",
        "MIDDLE SNAKE",
        "13334300",
        -117.2966,
        46.0376,
    ),
    "COWLITZ SALMON HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "COWLITZ_SALMON_HATCHERY",
        "COWLITZ",
        "14238000",
        -122.6293,
        46.5113,
    ),
    "DUNGENESS HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "DUNGENESS_HATCHERY",
        "ELWHA-DUNGENESS",
        "12048000",
        -123.1406,
        48.028,
    ),
    "EASTBANK HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "EASTBANK_HATCHERY",
        "MOSES COULEE",
        "",
        -120.2892,
        47.5336,
    ),
    "ELWHA HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "ELWHA_HATCHERY",
        "ELWHA-DUNGENESS",
        "12045500",
        -123.5493,
        48.1152,
    ),
    "FORKS CREEK HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "FORKS_CREEK_HATCHERY",
        "WILLAPA",
        "12013500",
        -123.5948,
        46.558,
    ),
    "GARRISON HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "GARRISON_HATCHERY",
        "CHAMBERS-CLOVER",
        "",
        -122.5741,
        47.1915,
    ),
    "GEORGE ADAMS HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "GEORGE_ADAMS_HATCHERY",
        "SKOKOMISH-DOSEWALLIPS",
        "12061500",
        -123.1818,
        47.3013,
    ),
    "HOODSPORT HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "HOODSPORT_HATCHERY",
        "SKOKOMISH-DOSEWALLIPS",
        "",
        -123.1399,
        47.407,
    ),
    "HUMPTULIPS HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "HUMPTULIPS_HATCHERY",
        "LOWER CHEHALIS",
        "12039005",
        -123.9892,
        47.2332,
    ),
    "HURD CREEK HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "HURD_CR_HATCHERY",
        "ELWHA-DUNGENESS",
        "12048000",
        -123.1433,
        48.1197,
    ),
    "ICY CREEK HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "ICY_CR_HATCHERY",
        "DUWAMISH-GREEN",
        "12113000",
        -121.9786,
        47.2799,
    ),
    "ISSAQUAH HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "ISSAQUAH_HATCHERY",
        "CEDAR-SAMMAMISH",
        "",
        -122.0386,
        47.5295,
    ),
    "KENDALL CREEK HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "KENDALL_CR_HATCHERY",
        "NOOKSACK",
        "12205000",
        -122.142,
        48.8973,
    ),
    "LEWIS RIVER HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "LEWIS_RIVER_HATCHERY",
        "LEWIS",
        "14220500",
        -122.6165,
        45.937,
    ),
    "LYONS FERRY HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "LYONS_FERRY_HATCHERY",
        "LOWER SNAKE",
        "13352600",
        -118.2287,
        46.5969,
    ),
    "MARBLEMOUNT HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "MARBLEMOUNT_HATCHERY",
        "UPPER SKAGIT",
        "12182500",
        -121.4178,
        48.5223,
    ),
    "MCKERNAN HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "MCKERNAN_HATCHERY",
        "SKOKOMISH-DOSEWALLIPS",
        "12061500",
        -123.203,
        47.3066,
    ),
    "MINTER CREEK HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "MINTER_CR_HATCHERY",
        "KITSAP",
        "",
        -122.7026,
        47.3726,
    ),
    "NASELLE HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "NASELLE_HATCHERY",
        "WILLAPA",
        "12010000",
        -123.7531,
        46.3722,
    ),
    "NEMAH HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "NEMAH_HATCHERY",
        "WILLAPA",
        "",
        -123.8411,
        46.503,
    ),
    "NORTH TOUTLE HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "NORTH_TOUTLE_HATCHERY",
        "COWLITZ",
        "14240525",
        -122.572,
        46.3746,
    ),
    "PRIEST RAPIDS HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "PRIEST_RAPIDS_HATCHERY",
        "ESQUATZEL COULEE",
        "12472800",
        -119.8967,
        46.6486,
    ),
    "REITER PONDS": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "REITER_PONDS",
        "SNOHOMISH",
        "12134500",
        -121.6241,
        47.839,
    ),
    "RINGOLD SPRINGS HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "RINGOLD_SPRINGS_HATCHERY",
        "ESQUATZEL COULEE",
        "12472800",
        -119.2612,
        46.5146,
    ),
    "SAMISH HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "SAMISH_HATCHERY",
        "LOWER SKAGIT-SAMISH",
        "12201500",
        -122.3315,
        48.5649,
    ),
    "SKAMANIA HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "SKAMANIA_HATCHERY",
        "SALMON-WASHOUGAL",
        "",
        -122.2179,
        45.6208,
    ),
    "SKOOKUMCHUCK HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "SKOOKUMCHUCK_HATCHERY",
        "UPPER CHEHALIS",
        "12026400",
        -122.7255,
        46.79,
    ),
    "SOOS CREEK HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "SOOS_CREEK_HATCHERY",
        "DUWAMISH-GREEN",
        "12113000",
        -122.1688,
        47.3093,
    ),
    "SPEELYAI HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "SPEELYAI_HATCHERY",
        "LEWIS",
        "",
        -122.4053,
        45.9887,
    ),
    "TOKUL CREEK HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "TOKUL_CR_HATCHERY",
        "SNOHOMISH",
        "12144500",
        -121.8397,
        47.5536,
    ),
    "TUCANNON HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "TUCANNON_HATCHERY",
        "MIDDLE SNAKE",
        "13344500",
        -117.6628,
        46.3201,
    ),
    "TUMWATER FALLS HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "TUMWATER_FALLS_HATCHERY",
        "DESCHUTES",
        "",
        -122.9043,
        47.0144,
    ),
    "VOIGHTS CREEK HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "VOIGHTS_CR_HATCHERY",
        "PUYALLUP-WHITE",
        "12096500",
        -122.1775,
        47.0828,
    ),
    "WASHOUGAL HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "WASHOUGAL_HATCHERY",
        "SALMON-WASHOUGAL",
        "",
        -122.166,
        45.6518,
    ),
    "FOSTER RD TRAP": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "FOSTER_RD_TRAP",
        "GRAYS-ELOCHOMAN",
        "",
        -123.371964,
        46.226517,
    ),
    "KALAMA FALLS HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "KALAMA_FALLS_HATCHERY",
        "LEWIS",
        "",
        -122.73316,
        46.016026,
    ),
    "LK ABERDEEN HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "LK_ABERDEEN_HATCHERY",
        "LOWER CHEHALIS",
        "",
        -123.742635,
        46.980079,
    ),
    "MERWIN DAM FCF": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "MERWIN_DAM_FCF",
        "LEWIS",
        "14220500",
        -122.555653,
        45.956563,
    ),
    "MODROW TRAP": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "MODROW_TRAP",
        "LEWIS",
        "",
        -122.838527,
        46.044736,
    ),
    "SOLDUC HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "SOLDUC_HATCHERY",
        "SOLEDUCK-HOH",
        "",
        -124.306113,
        48.054483,
    ),
    "SUNSET FALLS FCF": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "SUNSET_FALLS_FCF",
        "SNOHOMISH",
        "12134500",
        -121.550793,
        47.803818,
    ),
    "WALLACE R HATCHERY": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "WALLACE_R_HATCHERY",
        "SNOHOMISH",
        "12134500",
        -121.717,
        47.8674,
    ),
    "WASHOUGAL RIVER FISH WEIR": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "WASHOUGAL_RIVER_FISH_WEIR",
        "SALMON-WASHOUGAL",
        "",
        -122.255633,
        45.618172,
    ),
    "WHITEHORSE POND": HatcheryConfig(
        Provider(HatcheryProvider.WA_HATCHERY_DATA),
        "WHITEHORSE_POND",
        "STILLIGUAMISH",
        "12167000",
        -121.720542,
        48.27576,
    ),
}

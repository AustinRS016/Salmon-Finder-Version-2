from dataclasses import dataclass, field
from flask import Flask, Response
from config import hatcheries
from dataclasses_json import config, dataclass_json

import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


@dataclass_json
@dataclass
class HatcheryFeatureProperties:
    facility_name: str = field(metadata=config(field_name="Facility Name"))
    facility: str = field(metadata=config(field_name="Facility"))
    wria: str = field(metadata=config(field_name="WRIA"))
    river_gauge: str


@dataclass_json
@dataclass
class HatcheryFeatureGeometry:
    type: str
    coordinates: list[float]


@dataclass_json
@dataclass
class HatcheryFeature:
    type: str
    properties: HatcheryFeatureProperties
    geometry: HatcheryFeatureGeometry


@dataclass_json
@dataclass
class HatcheryGeoJson:
    type: str
    features: list[HatcheryFeature]


@dataclass_json
@dataclass
class HatcheryConfigCleaned:
    facility: str
    wria: str
    river_gauge: str
    lat: float
    long: float


@app.route("/mapconfig")
def get_map_config():
    res = HatcheryGeoJson(
        "FeatureCollection",
        features=[
            HatcheryFeature(
                type="Feature",
                properties=HatcheryFeatureProperties(
                    key, value.facility, value.wria, value.river_gauge
                ),
                geometry=HatcheryFeatureGeometry("Point", [value.lat, value.long]),
            )
            for key, value in hatcheries.items()
        ],
    )
    return Response(res.to_json(), content_type="application/geo+json")


if __name__ == "__main__":
    app.run(debug=True)

import boto3
import logging
import os

from config import hatcheries
from dataclasses_json import config, dataclass_json
from dataclasses import dataclass, field
from dotenv import load_dotenv
from flask import Flask, Response, json
from flask_cors import CORS

load_dotenv()

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
cors = CORS(app, origins=["http://localhost:3000"])


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
class Count:
    species: str
    run: str
    origin: str


@dataclass_json
@dataclass
class DateCount:
    date: str
    count: int


@dataclass_json
@dataclass
class YearCount:
    year: int
    count: int


@dataclass_json
@dataclass
class DayCount:
    day: int
    count: int


@dataclass_json
@dataclass
class RecentDailyEscapementCount(Count):
    date_counts: list[DateCount]


@dataclass_json
@dataclass
class HistoricalYearlyCount(Count):
    year_counts: list[YearCount]


@dataclass_json
@dataclass
class HistoricalDailyAverageCount(Count):
    day_counts: list[DayCount]


@dataclass_json
@dataclass
class HatcheryData:
    historical_yearly_counts: list[HistoricalYearlyCount]
    historical_daily_average_counts: list[HistoricalDailyAverageCount]
    recent_daily_escapement_counts: list[RecentDailyEscapementCount]


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


@app.route("/hatchery/<facility>")
def get_hatchery(facility):
    session = boto3.Session(
        aws_access_key_id=os.getenv("BUCKETEER_AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("BUCKETEER_AWS_SECRET_ACCESS_KEY"),
    )
    s3 = session.resource("s3")

    object_bargraph = s3.Object(
        bucket_name=os.getenv("BUCKETEER_BUCKET_NAME"),
        key=f"{facility}_bargraph",
    ).get()

    bargraph_json = json.loads(object_bargraph["Body"].read())

    object_denisty_estimation = s3.Object(
        bucket_name=os.getenv("BUCKETEER_BUCKET_NAME"),
        key=f"{facility}_density_estimation",
    ).get()

    density_estimation = json.loads(object_denisty_estimation["Body"].read())

    object_recent_escapement = s3.Object(
        bucket_name=os.getenv("BUCKETEER_BUCKET_NAME"),
        key=f"{facility}_recent_escapement",
    ).get()

    recent_escapement_json = json.loads(object_recent_escapement["Body"].read())

    res = HatcheryData(
        [
            HistoricalYearlyCount(
                el["species"],
                el["run"],
                el["origin"],
                [
                    YearCount(year_count["year"], year_count["count"])
                    for year_count in el["year_counts"]
                ],
            )
            for el in bargraph_json
        ],
        [
            HistoricalDailyAverageCount(
                el["species"],
                el["run"],
                el["origin"],
                [
                    DayCount(day_count["day"], day_count["count"])
                    for day_count in el["density_data"]
                ],
            )
            for el in density_estimation
        ],
        [
            RecentDailyEscapementCount(
                el["species"],
                el["run"],
                el["origin"],
                [
                    DateCount(date_count["day"], date_count["count"])
                    for date_count in el["day_counts"]
                ],
            )
            for el in recent_escapement_json
        ],
    )

    return Response(res.to_json())


if __name__ == "__main__":
    app.run(debug=True)

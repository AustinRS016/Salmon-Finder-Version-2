import boto3
import os

from dotenv import load_dotenv

from ...config.config import hatcheries, reduced_coordinates_dict
from .lib import get_weather

load_dotenv()

for hatchery_name, config in hatcheries.items():
    session = boto3.Session(
        aws_access_key_id=os.getenv("BUCKETEER_AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("BUCKETEER_AWS_SECRET_ACCESS_KEY"),
    )
    s3 = session.resource("s3")
    lon, lat = reduced_coordinates_dict.get(config.reduced_coordinate_key)

    weather = get_weather(lat, lon)

    print(weather)

    object_weather = s3.Object(
        bucket_name=os.getenv("BUCKETEER_BUCKET_NAME"),
        key=f"{config.facility}_weather",
    )

    object_weather.put(Body=weather)

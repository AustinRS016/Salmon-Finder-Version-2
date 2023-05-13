import boto3
import os

from dotenv import load_dotenv

from config import hatcheries
from create_graph_data import compute_bargraph_data, get_rolling_average

load_dotenv()

for hatchery_name, provider in hatcheries.items():
    hatchery_provider_response = provider.hatchery_provider.value.get_hatchery_data(
        hatchery_name
    )

    # Outputs as JSON
    bargraph = compute_bargraph_data(hatchery_provider_response)
    rolling_average = get_rolling_average(hatchery_provider_response)

    session = boto3.Session(
        aws_access_key_id=os.getenv("BUCKETEER_AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("BUCKETEER_AWS_SECRET_ACCESS_KEY"),
    )
    s3 = session.resource("s3")

    object_bargraph = s3.Object(
        bucket_name=os.getenv("BUCKETEER_BUCKET_NAME"),
        key=f"{hatchery_name.replace(' ', '_')}_bargraph",
    )

    object_bargraph.put(Body=bargraph)

    object_rolling_average = s3.Object(
        bucket_name=os.getenv("BUCKETEER_BUCKET_NAME"),
        key=f"{hatchery_name.replace(' ', '_')}_rolling_average",
    )

    object_rolling_average.put(Body=rolling_average)

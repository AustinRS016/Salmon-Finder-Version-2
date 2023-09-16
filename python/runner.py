import boto3
import os

from dotenv import load_dotenv

from config import hatcheries
from create_graph_data import (
    compute_bargraph_data,
    compute_KDE,
    get_recent_escapement,
)

load_dotenv()

for hatchery_name, config in hatcheries.items():
    hatchery_provider_response = (
        config.provider.hatchery_provider.value.get_hatchery_data(
            config.facility.replace("_", " ")
        )
    )

    # Outputs as JSON
    bargraph = compute_bargraph_data(hatchery_provider_response)
    density_estimation = compute_KDE(hatchery_provider_response)
    recent_escapement = get_recent_escapement(hatchery_provider_response)

    session = boto3.Session(
        aws_access_key_id=os.getenv("BUCKETEER_AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("BUCKETEER_AWS_SECRET_ACCESS_KEY"),
    )
    s3 = session.resource("s3")

    object_bargraph = s3.Object(
        bucket_name=os.getenv("BUCKETEER_BUCKET_NAME"),
        key=f"{config.facility}_bargraph",
    )

    object_bargraph.put(Body=bargraph)

    object_density_estimation = s3.Object(
        bucket_name=os.getenv("BUCKETEER_BUCKET_NAME"),
        key=f"{config.facility}_density_estimation",
    )

    object_density_estimation.put(Body=density_estimation)

    object_recent_escapement = s3.Object(
        bucket_name=os.getenv("BUCKETEER_BUCKET_NAME"),
        key=f"{config.facility}_recent_escapement",
    )

    object_recent_escapement.put(Body=recent_escapement)

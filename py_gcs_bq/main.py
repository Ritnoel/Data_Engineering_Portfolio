from google.cloud import bigquery, storage
from api import GameAPI
from sandbox import (
    load_data_from_gcs,
    create_bigquery_dataset,
    create_bigquery_table,
    create_bucket,
    load_to_bucket,
    load_data_from_local,
)
import os
from dotenv import load_dotenv
import config


load_dotenv()

GOOGLE_AUTH_FILE = os.environ["GOOGLE_AUTH_FILE"]
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_AUTH_FILE

# Instantiate  client
client_bq = bigquery.Client(project=config.PROJECT_ID)
client_gcs = storage.Client(project=config.PROJECT_ID)

# Create a bucket
create_bucket(client_gcs, config.STORAGE_CLASS, config.LOCATION, config.BUCKET_NAME)

# Create a dataset
create_bigquery_dataset(client_bq, config.DATASET_ID)

# Create table
create_bigquery_table(client_bq, config.PROJECT_ID, config.DATASET_ID, config.TABLE_ID)

# Load CSV from Local
load_data_from_local(client_bq, config.PROJECT_ID, config.DATASET_ID, config.TABLE_ID, config.SCHEMA_LOCAL, config.FILE_PATH)

# Load API to Bucket
game = GameAPI(config.URL)
response = game.get(config.ENDPOINT)
jsonl_data = game._to_jsonl_buffer(response)
bucket_uri = load_to_bucket(client_gcs, config.BUCKET_NAME, config.FILE_NAME, jsonl_data)

# Load from Bucket to Bigquery
load_data_from_gcs(client_bq, config.PROJECT_ID, config.DATASET_ID, config.TABLE_ID, config.SCHEMA_API, bucket_uri)
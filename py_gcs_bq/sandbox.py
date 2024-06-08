from google.cloud import bigquery, storage
from google.cloud.exceptions import Conflict
from dotenv import load_dotenv
import logging
import json


logging.basicConfig(filename="logs.log", level=logging.INFO)


# Create a dataset(schema)

def create_bigquery_dataset(client, dataset):
    try:
        dataset_ref = client.dataset(dataset)
        dataset = bigquery.Dataset(dataset_ref)
        dataset = client.create_dataset(dataset_ref)
        logging.info(f"{dataset} dataset created succesfully")
    except Conflict:
        logging.info(f"{dataset} already exist, exitting successfully")
    except Exception as e:
        logging.error(f"An error occurred creating the {dataset}: {e}")

# Create a table
def create_bigquery_table(client, project_id, dataset_id, table_id):
    try:
        with open("schema.json", "r") as f:
            data = f.read()
            schema = json.loads(data)
        table_ref = f"{project_id}.{dataset_id}.{table_id}"
        table = bigquery.Table(table_ref, schema=schema)
        client.create_table(table)
        logging.info(f"{table_id} has been created")
    except Conflict:
        logging.info(f"{table_id} already exist, exitting successfully")
    except Exception as e:
        logging.error(f"An error occurred creating the {table_id}: {e}")
    
    


# Create a bucket
def create_bucket(
    client,
    storage_class,
    location,
    bucket_name,
):
    try:
        bucket = storage.Bucket(client, bucket_name)
        bucket.storage_class = storage_class
        bucket.location = location
        client.create_bucket(bucket)
        logging.info(f"{bucket_name} has been created")
    except Conflict:
        logging.info(f"{bucket_name} already exist, exitting successfully")
    except Exception as e:
        logging.error(f"An error occurred creating the {bucket_name}: {e}")

# load to bucket
def load_to_bucket(client, bucket_name, filename, filepath):
    try:
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(filename)
        blob.upload_from_filename(filepath)
        logging.info(f"{bucket_name} has been loaded")
        return f"gs://{bucket_name}/{filename}"
    except Conflict:
        logging.info(f"{bucket_name} already exist, exitting successfully")
    except Exception as e:
        logging.error(f"An error occurred creating the {bucket_name}: {e}")


# Loading data from gcs
def load_data_from_gcs(
    client,
    project_id: str,
    dataset_id: str,
    table_id: str,
    schema: str,
    source_uri: str,
):
    try:
        with open(schema, "r") as file:
            schema_json = json.load(file)

        job_config = bigquery.LoadJobConfig(
            schema=schema_json, source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
        )
        table_ref = f"{project_id}.{dataset_id}.{table_id}"
        load_job = client.load_table_from_uri(source_uri, table_ref, job_config=job_config)
        load_job.result()
        logging.info(f"Loaded {load_job.output_rows} rows into {dataset_id}:{table_id}.")
    except Exception as e:
        logging.error(f"An error occurred creating the loading to gcs: {e}")

# Load data from local
def load_data_from_local(
    client,
    project_id: str,
    dataset_id: str,
    table_id: str,
    schema: str,
    local_path: str,
):
    try:
        with open(schema, "r") as file:
            schema_json = json.load(file)

        job_config = bigquery.LoadJobConfig(
            schema=schema_json, source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_CSV
        )

        table_ref = f"{project_id}.{dataset_id}.{table_id}"
        load_job = client.load_table_from_file(local_path, table_ref, job_config=job_config)
        load_job.result()
        logging.info(f"Loaded {load_job.output_rows} rows into {dataset_id}:{table_id}.")
    except Conflict:
        logging.info(f"{table_id} already exist, exitting successfully")
    except Exception as e:
        logging.error(f"An error occurred creating the {table_id}: {e}")

from google.oauth2 import service_account
from google.cloud import bigquery
from query import QUERY
from dotenv import load_dotenv
import os

load_dotenv()  # Loads .env variables

SERVICE_ACCOUNT_KEY_FILE = os.environ.get("SERVICE_ACCOUNT_KEY_FILE")
PROJECT_ID = os.environ.get("PROJECT_ID")

def get_dataset():
    """
    Fetches the dataset from BigQuery using the provided query.
    This function executes a predefined SQL query against a BigQuery dataset
    and returns the results as a list of dictionaries.
    The query is defined in the `query` module, which should be imported
    at the beginning of this file.
    The service account credentials are loaded from the environment variable
    `SERVICE_ACCOUNT_KEY_FILE`, which should point to a JSON file containing
    Returns:
        list: A list of dictionaries representing the rows in the dataset.
    """
    # Create credentials using the service account key
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_KEY_FILE
    )
    # Create a BigQuery client using the credentials
    client = bigquery.Client(credentials=credentials, project=PROJECT_ID)
    query_job = client.query(QUERY)  # Make an API request
    results = query_job.result()  # Wait for the job to complete
    return [dict(row) for row in results]



get_dataset()

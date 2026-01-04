from etl.extract import extract_sales_data
from etl.transform import transform_sales_data
from etl.load import load_to_db
import logging
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

user = os.getenv("DB_USER")
password = quote_plus(os.getenv("DB_PASSWORD"))
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db = os.getenv("DB_NAME")

# making sure logs directory exists
os.makedirs("logs", exist_ok=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RAW_FILE_PATH = os.path.join(
    BASE_DIR, "data", "raw", "sales_raw.csv"
)

logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DB_URL = f"postgresql://{user}:{password}@{host}:{port}/{db}"

def main():
    logging.info("ETL job started")

    df = extract_sales_data(RAW_FILE_PATH)
    logging.info(f"Extracted {len(df)} rows")

    df_clean = transform_sales_data(df)
    logging.info(f"Transformed {len(df_clean)} rows")

    load_to_db(df_clean, DB_URL)
    logging.info("ETL job completed successfully}")

    # --- HEARTBEAT LOG ---
    with open("/home/inikh/projects/etl-sales-pipeline/logs/etl.log", "a") as f:
        f.write(f"ETL ran successfully at {datetime.now()}\n")

if __name__ == "__main__":
    main()
# End-to-End ETL Sales Pipeline

## Overview
This project implements a complete ETL pipeline that ingests raw sales data,
performs data cleaning and transformations, and loads it into a relational database.

## Tech Stack
- Python
- Pandas
- SQL (PostgreSQL/MySQL)
- Git

## Pipeline Flow
1. Extract data from CSV
2. Transform (deduplication, null handling, type casting, normalization)
3. Load into database

## Data Quality Checks
- Duplicate order_id removal
- Null handling
- Date format normalization
- Validation before load

## How to Run
```bash
pip install -r requirements.txt
python run_etl.py
```

## Project Structure
- Check project-structure file





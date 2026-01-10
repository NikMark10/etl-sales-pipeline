# End-to-End ETL Sales Pipeline

## Overview
This project implements a complete ETL pipeline that ingests fashion data from api,
performs data cleaning and transformations, and loads it into a relational database.

## Tech Stack
- Python
- Pandas
- SQL (PostgreSQL/MySQL)
- Git

## Pipeline Flow
1. Extract data from API (https://fakestoreapi.com/products)
2. Transform (just renaming columns for now)
3. Load into database

## How to Run
```bash
pip install -r requirements.txt
python run_etl.py

or

Create windows scheduler and add the batch file from project to it
```

## Project Structure
- Check project-structure file







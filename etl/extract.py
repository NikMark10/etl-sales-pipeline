import pandas as pd

file_path = r"C:\Users\inikh\Documents\myProjects\etl-sales-pipeline\data\raw\sales_raw.csv"

def extract_sales_data(file_path):
    df = pd.read_csv(file_path)
    return df
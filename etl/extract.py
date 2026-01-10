import requests
import pandas as pd

def extract_sales_data():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("API call failed")
    
    data = response.json()
    df = pd.DataFrame(data)

    return df
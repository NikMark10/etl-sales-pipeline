import pandas as pd

def transform_sales_data(df):
    # 1. Deduplication
    df = df.drop_duplicates(subset=["order_id"]).copy()
    df.loc[:, "amount"] = df["amount"].fillna(0)

    # 2. Null handling
    df["amount"] = df["amount"].fillna(0)
    df = df.dropna(subset=["order_id", "order_date"])

    # 3. Type conversions
    df.loc[:, "order_date"] = pd.to_datetime(
        df["order_date"],
        format="mixed",
        dayfirst=True,
        errors="coerce"
        )
    df["amount"] = df["amount"].astype(float)

    # 4. Handling cases
    df["country"] = df["country"].str.lower()

    assert df["order_id"].isnull().sum() == 0
    assert (df["amount"] >= 0).all()

    return df
def transform_sales_data(df):
    df = df[['id', 'price', 'category', 'title']].copy()
    
    df = df.rename(columns={
        'id': 'order_id',
        'price': 'amount'
    })

    df.loc[:, 'currency'] = 'USD'
    return df
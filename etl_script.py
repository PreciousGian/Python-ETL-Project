import pandas as pd
from sqlalchemy import create_engine

# Extract
df = pd.read_csv('data/products.csv')

# Transform
df['price'] = df['price'] * 1.12  # add tax
df['category'] = ['Electronics', 'Accessories', 'Accessories']

# Load
engine = create_engine('sqlite:///products.db')
df.to_sql('products', con=engine, if_exists='replace', index=False)
print("ETL process completed successfully!")


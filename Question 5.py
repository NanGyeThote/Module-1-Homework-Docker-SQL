import pandas as pd
from sqlalchemy import create_engine
import argparse
from time import time

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    csv_name = 'taxi_zone_lookup.csv'  # Make sure to provide the correct path to the CSV

    # Establish the connection to PostgreSQL
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Read the CSV in chunks
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    # Process the first chunk
    df = next(df_iter)

    # Create table if not exists and load the first chunk
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace', index=False)  # Ensure no index
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)  # Append data

    # Process remaining chunks
    while True:
        t_start = time()
        try:
            df = next(df_iter)
            df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
            t_end = time()
            print(f'Inserted another chunk... took {t_end - t_start:.3f} seconds')
        except StopIteration:
            break  # Stop when there are no more chunks to process

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest Taxi Zone Lookup CSV into PostgreSQL')

    parser.add_argument('--user', help='User name for Postgres')
    parser.add_argument('--password', help='Password for Postgres')
    parser.add_argument('--host', help='Host for Postgres')
    parser.add_argument('--port', help='Port for Postgres')
    parser.add_argument('--db', help='Database name for Postgres')
    parser.add_argument('--table_name', help='Table name to insert data into')

    args = parser.parse_args()
    main(args)

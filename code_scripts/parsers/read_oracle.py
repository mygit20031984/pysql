import pandas as pd
from sqlalchemy import create_engine
from code_scripts.Connection_Details.conn_oracle import username

# UN = username
# print(UN)


oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'

engine = create_engine(
    oracle_connection_string.format(
        username='system',
        password='oracle',
        hostname='localhost',
        port='1521',
        database='XE',
    )
)

data = pd.read_sql("SELECT * FROM tab1", engine)

data.to_csv('oracle_data.csv', index=False)

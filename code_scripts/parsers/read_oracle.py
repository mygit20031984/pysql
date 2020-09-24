import pandas as pd
from sqlalchemy import create_engine
from code_scripts.conn_oracle import username

UN = username
print(UN)


def read_oracle_df(UN, PWD, HN, SID, PORT, SQL):
    oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'

    engine = create_engine(
        oracle_connection_string.format(
            username=UN,
            password=PWD,
            hostname=HN,
            port=PORT,
            database=SID,
        )
    )
    query = SQL
    df = pd.read_sql(query, engine)
    return df

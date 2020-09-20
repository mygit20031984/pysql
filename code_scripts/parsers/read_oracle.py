import cx_Oracle
from sqlalchemy import create_engine

engine = create_engine('oracle://user:password@host_or_scan_address:1521/ORACLE_SERVIVE_NAME')

df = pd.read_sql('select * from table_name', engine)

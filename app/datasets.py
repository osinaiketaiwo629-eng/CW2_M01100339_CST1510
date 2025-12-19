import pandas as pd

def get_all_datasets_metadata(conn):
    sql_ = "SELECT * from datasets_metadata"
    data = pd.read_sql(sql_,conn) 
    return(data)


def migrate_datasets_metadata(conn):
    data = pd.read_csv('DATA/datasets_metadata.csv')
    data.to_sql('datasets_metadata', conn, if_exists='append', index=False)
    conn.close()    


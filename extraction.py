import pandas as pd
import clickhouse_connect
import sys
import json

CLICKHOUSE_CLOUD_HOSTNAME = 'github.demo.trial.altinity.cloud'
CLICKHOUSE_CLOUD_USER = 'demo'
CLICKHOUSE_CLOUD_PASSWORD = 'demo'




def extract_tripdata():
    client = clickhouse_connect.get_client(
        host=CLICKHOUSE_CLOUD_HOSTNAME, port=8443, username=CLICKHOUSE_CLOUD_USER, password=CLICKHOUSE_CLOUD_PASSWORD)

    print("connected to " + CLICKHOUSE_CLOUD_HOSTNAME + "\n")
    QUERY = "select pickup_date, pickup_datetime, dropoff_datetime from tripdata"
    result = client.query(QUERY) 
    sys.stdout.write("query: ["+QUERY + "] returns:\n\n")
    print(result.result_rows)
    # data = result.fetchall()
    # tripdata_df = pd.DataFrame(QUERY, columns=['pickup_date', 'pickup_datetime', 'dropoff_datetime'])
    # print(tripdata_df.to_string(index=False))
        

extract_tripdata()


# sys.stdout.write("query: ["+QUERY + "] returns:\n\n")
# print(result.result_rows)


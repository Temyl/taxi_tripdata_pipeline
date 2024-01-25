import sqlite3
# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from airflow.hooks.sqlite_hook import SqliteHook 
# import pandas as pd
from extraction import extract_tripdata
from sql_statements import raw_data, transformed_data

conn = sqlite3.connect('taxi_data_metrics.db')




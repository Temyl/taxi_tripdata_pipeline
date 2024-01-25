from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.sqlite_hook import SqliteHook 


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'tripdata_metrics',
    default_args=default_args,
    description='A DAG to fetch and write metrics to SQLite',
    schedule_interval='@once',
)

  # tasks are represented as operators
begin_execution = PythonOperator(task_id='begin_execution')



end_execution = PythonOperator(task_id= 'end_execution')


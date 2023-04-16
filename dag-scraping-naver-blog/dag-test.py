from datetime import datetime

from airflow.models import DAG

from airflow.providers.http.sensors.http import HttpSensor
from airflow.operators.python import PythonOperator


def print_hi():
    print('hi')


with DAG(
    dag_id='dag-test',
    schedule_interval='@daily',
    start_date=datetime(2023, 4, 1),
    catchup=False
) as dag:
    
    # is_available = HttpSensor(
    #     task_id='is-scraping-naver-blog-api-available',
    #     http_conn_id='test-connection',
    #     endpoint='/'
    # )
    
    # is_available
    
    h = PythonOperator(
        task_id='print-hi',
        python_callable=print_hi
    )
    
    h

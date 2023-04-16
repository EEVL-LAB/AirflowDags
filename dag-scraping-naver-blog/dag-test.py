from datetime import datetime

from airflow.models import DAG

from airflow.providers.http.sensors.http import HttpSensor


with DAG(
    dag_id='dag-test',
    schedule_interval='@daily',
    start_date=datetime(2023, 4, 1),
    catchup=False
) as dag:
    
    is_available = HttpSensor(
        task_id='is-scraping-naver-blog-api-available',
        http_conn_id='test-connection'
    )
    
    is_available

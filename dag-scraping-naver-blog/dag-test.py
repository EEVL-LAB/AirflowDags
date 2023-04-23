import time
import requests
import datetime
from typing import List
from airflow.models import DAG
from airflow.operators.python import PythonOperator


def request_naver_blog_into_kafka_provider(
    target_keywords: List[str]
):
    while True:
        time.sleep(60*10)
        break


with DAG(
    dag_id='dag-scraping-naver-blog-test',
    schedule_interval='@daily',
    start_date=datetime.datetime(2023, 4, 1),
    catchup=False,
    dagrun_timeout=datetime.timedelta(days=1)
) as dag:
    
    scraping_naver_blog_into_kafka_provider = PythonOperator(
        task_id='scraping_naver_blog_into_kafka_provider-test',
        execution_timeout=datetime.timedelta(days=1),
        sla=datetime.timedelta(days=1),
        python_callable=request_naver_blog_into_kafka_provider,
        op_kwargs={
            "target_keywords": [
                '윤석열',
                '오늘수거'
            ]
        }
    )
    
    scraping_naver_blog_into_kafka_provider

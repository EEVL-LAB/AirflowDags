import requests
import datetime
from typing import List
from airflow.models import DAG
from airflow.operators.python import PythonOperator


def request_naver_blog_into_kafka_provider(
    target_keywords: List[str]
):
    today = datetime.date.today()
    delta = datetime.timedelta(days=1)
    date = str(today - delta)
    for target_keyword in target_keywords:
        response = requests.post(
            url='http://scraping.eevl.studio:8080/scraping_naver_blog',
            json={
                'target_keyword': target_keyword,
                'start_date': date,
                'end_date': date,
                "page_limit": 100
            }
        )
        print(response)


with DAG(
    dag_id='dag-scraping-naver-blog',
    schedule_interval='@daily',
    start_date=datetime.datetime(2023, 4, 1),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(days=1)
) as dag:
    
    scraping_naver_blog_into_kafka_provider = PythonOperator(
        task_id='scraping_naver_blog_into_kafka_provider',
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

import json

from datetime import datetime

from airflow.models import DAG

from airflow.operators.python import PythonOperator
# from airflow.providers.http.sensors.http import HttpSensor
# from airflow.providers.http.operators.http import SimpleHttpOperator

import requests


def request_naver_blog_into_kafka_provider(
    target_keyword: str,
    start_date: str,
    end_date: str
):
    requests.post(
        url='http://scraping.eevl.studio:8080/scraping_naver_blog',
        json={
            'target_keyword': target_keyword,
            'start_date': start_date,
            'end_date': end_date
        }
    )


with DAG(
    dag_id='dag-scraping-naver-blog',
    schedule_interval='@daily',
    start_date=datetime(2023, 4, 1),
    catchup=False
) as dag:
    
    # is_scraping_naver_blog_api_available = HttpSensor(
    #     task_id='is-scraping-naver-blog-api-available',
    #     http_conn_id='scraping-into-kafka-provider',
    #     endpoint='/scraping_naver_blog'
    # )
    
    # scraping_naver_blog_into_kafka_provider = SimpleHttpOperator(
    #     task_id='scraping-naver-blog-into-kafka-provider',
    #     http_conn_id='scraping-into-kafka-provider',
    #     endpoint='/scraping_naver_blog',
    #     method='POST',
    #     data={
    #         'target_keyword': '윤석열',
    #         'start_date': '2022-04-14',
    #         'end_date': '2022-06-14'
    #     },
    #     response_filter=lambda res: json.loads(res.text),
    #     log_response=True
    # )
    
    # is_scraping_naver_blog_api_available >> scraping_naver_blog_into_kafka_provider
    # scraping_naver_blog_into_kafka_provider
    
    scraping_naver_blog_into_kafka_provider = PythonOperator(
        task_id='scraping_naver_blog_into_kafka_provider',
        python_callable=request_naver_blog_into_kafka_provider,
        op_kwargs={
            "target_keyword": "윤석열",
            "start_date": "2023-01-01",
            "end_date": "2023-04-15"
        }
    )
    
    scraping_naver_blog_into_kafka_provider

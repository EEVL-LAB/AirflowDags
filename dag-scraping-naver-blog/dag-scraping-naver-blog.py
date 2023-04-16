import json

from datetime import datetime

from airflow.models import DAG

from airflow.operators.python import PythonOperator
# from airflow.providers.http.sensors.http import HttpSensor
# from airflow.providers.http.operators.http import SimpleHttpOperator

from scripts.api import *


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
        python_callable=request_naver_blog_into_kafka_provider
    )
    
    scraping_naver_blog_into_kafka_provider

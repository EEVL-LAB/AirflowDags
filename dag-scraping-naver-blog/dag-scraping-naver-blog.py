from airflow.models import DAG

from airflow.operators.python import PythonOperator

from airflow.providers.http.operators.http import SimpleHttpOperator


with DAG(
    dag_id='dag-scraping-naver-blog',
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    scraping_naver_blog_into_kafka_provider = SimpleHttpOperator(
        task_id='scraping-naver-blog-into-kafka-provider',
        http_conn_id='scraping-into-kafka-provider',
        endpoint='scraping_naver_blog',
        data={
            'target_keyword': '윤석열',
            'start_date': '2022-04-14',
            'end_date': '2022-06-14'
        },
        log_response=True
    )
    
    scraping_naver_blog_into_kafka_provider

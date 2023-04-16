import requests


def request_naver_blog_into_kafka_provider(
    target_keyword: str,
    start_date: str,
    end_date: str
):
    requests.post(
        url='http://scraping.eevl.studio:8080/scraping_naver_blog',
        data={
            'target_keyword': target_keyword,
            'start_date': start_date,
            'end_date': end_date
        }
    )

from elasticsearch import Elasticsearch

from config.settings import env

es = Elasticsearch(
    hosts=[f"http://{env('ELASTIC_HOST')}:9200"],
    basic_auth=(env("ELASTIC_USER"), env("ELASTIC_PASSWORD")),
)

from elasticsearch import helpers, Elasticsearch

from cocksearcher.domain.cocktail import Cocktail

from dataclasses import asdict

from cocksearcher.settings import env


class CocktailESRepository:

    def __init__(self):
        self.es = Elasticsearch(
            hosts=[f"http://{env('ELASTIC_HOST')}:9200"],
            basic_auth=(env("ELASTIC_USER"), env("ELASTIC_PASSWORD")),
        )

    def insert(self, cocktail: Cocktail):
        doc = asdict(cocktail)

        self.es.index(index="cocktails", doc_type="_doc", body=doc)

    def insert_all(self, cocktails: list[Cocktail]):
        docs = ({"_index": "cocktails", "_source": asdict(doc)} for doc in cocktails)
        helpers.bulk(self.es, docs)

    def get(self, cocktail_id: int):
        pass

    def get_all(self):
        pass

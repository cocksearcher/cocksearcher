from elasticsearch import helpers, Elasticsearch

from cocksearcher.infrastructures.cockdb.cocktail import Cocktail

from dataclasses import asdict

from cocksearcher.settings import env


class CocktailESRepository:

    def __init__(self):
        self.es = Elasticsearch(
            hosts=[f"http://{env('ELASTIC_HOST')}:9200"],
            basic_auth=(env("ELASTIC_USER"), env("ELASTIC_PASSWORD")),
        )
        self.index = "cocktails"

    def insert(self, cocktail: Cocktail):
        doc = asdict(cocktail)

        self.es.index(index=self.index, doc_type="_doc", body=doc)

    def insert_all(self, cocktails: list[Cocktail]):
        docs = ({"_index": self.index, "_source": asdict(doc)} for doc in cocktails)
        helpers.bulk(self.es, docs)

    def update_mood(self, cocktails: list[Cocktail]):
        for cocktail in cocktails:
            self.es.update(index=self.index, doc_type="_doc", id=cocktail.id, body={"doc": {"mood": cocktail.mood}})

    def get(self, cocktail_id: int):
        pass

    def get_all(self, filters):
        pass

    def remove_all(self):
        self.es.options(ignore_status=[400, 404]).indices.delete(index=self.index)

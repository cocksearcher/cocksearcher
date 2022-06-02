from elasticsearch import helpers

from cocksearcher.domain.cocktail import Cocktail
from cocksearcher.domain.repositories.cocktail import CocktailRepository

from dataclasses import asdict

from cocksearcher.infrastructures.elasticsearch.elasticsearch import es


class CocktailESRepository(CocktailRepository):
    def insert(self, cocktail: Cocktail):
        doc = asdict(cocktail)

        es.index(index="cocktails", doc_type="_doc", body=doc)

    def insert_all(self, cocktails: list[Cocktail]):
        docs = ({"_index": "cocktails", "_source": asdict(doc)} for doc in cocktails)
        helpers.bulk(es, docs)

    def get(self, cocktail_id: int):
        pass

    def get_all(self):
        pass

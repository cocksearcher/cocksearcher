from cocksearcher.domain.cocktail_repository import CocktailRepository
from config.services import BaseService


class CocktailListService(BaseService):

    dependency_interfaces = (CocktailRepository,)

    def __init__(self, cocktail_repository):
        self.check_dependencies(cocktail_repository)

        self.cocktail_repository: CocktailRepository = cocktail_repository


    def refresh(self):
        self.cocktail_repository.create_all()
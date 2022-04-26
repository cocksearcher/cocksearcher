from django.urls import path

from cocksearcher.views.v1.cocktail_detail import CocktailDetailView
from cocksearcher.views.v1.cocktail_list import CocktailListView
from cocksearcher.views.v1.cocktail_prefer import CocktailPreferView
from cocksearcher.views.v1.today_cocktail import TodayCocktailView

urlpatterns = [
    path('cocktail', CocktailListView.as_view(), "cocktail-list"),
    path('cocktail/<int:id>/prefer', CocktailPreferView.as_view(), "cocktail-prefer"),
    path('cocktail/<int:id>', CocktailDetailView.as_view(), "cocktail-detail"),
    path('cocktail/today', TodayCocktailView.as_view(), "today-cocktail"),
]

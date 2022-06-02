from django.urls import path

from cocksearcher.views.v1.cocktail_detail import CocktailDetailView
from cocksearcher.views.v1.cocktail_list import CocktailListView
from cocksearcher.views.v1.cocktail_list_refresh import CocktailListRefreshView
from cocksearcher.views.v1.cocktail_prefer import CocktailPreferView
from cocksearcher.views.v1.today_cocktail import TodayCocktailView

urlpatterns = [
    path('cocktails', CocktailListView.as_view(), name="cocktail-list"),
    path('cocktails/<int:id>/prefer', CocktailPreferView.as_view(), name="cocktail-prefer"),
    path('cocktails/<int:id>', CocktailDetailView.as_view(), name="cocktail-detail"),
    path('cocktails/today', TodayCocktailView.as_view(), name="today-cocktail"),
    path('cocktails/refresh', CocktailListRefreshView.as_view(), name="cocktail-refresh")
]

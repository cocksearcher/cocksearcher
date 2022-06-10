from django.urls import path

from list.views import CocktailListView, CocktailListRefreshView

urlpatterns = [
    path('', CocktailListView.as_view(), name="cocktail-list"),
    path('refresh', CocktailListRefreshView.as_view(), name="cocktail-list-refresh")
]

from django.urls import path

from cocktail.views import CocktailDetailView, CocktailPreferView

urlpatterns = [
    path('', CocktailDetailView.as_view(), name="cocktail-detail"),
    path('prefer', CocktailPreferView.as_view(), name="cocktail-prefer")
]

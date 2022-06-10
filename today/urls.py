from django.urls import path

from today.views import TodayCocktailView

urlpatterns = [
    path('', TodayCocktailView.as_view(), name="today-cocktail")
]
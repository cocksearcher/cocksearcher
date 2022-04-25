from django.contrib import admin
from django.urls import path

from cocksearcher.views.v1.today_cocktail import TodayCocktailView

urlpatterns = [
    path('cocktail/today', TodayCocktailView.as_view()),
    path('admin/', admin.site.urls)
]

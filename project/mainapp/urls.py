from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.index_cite, name="index"),
    path("history/", views.history, name="history"),
    path("history/<int:age>/", views.history_info, name="history_info"),
    path("cities/", views.cities, name="cities"),
    path("cities/<slug:city>/", views.city_info, name="city_info"),
    path("cities/<slug:city>/<int:year>/", views.city_year, name="city_year"),
    path("facts/", views.facts, name="facts"),
    path("cities/paris/", views.paris, name="paris"),
    path("cities/marseille/", views.marseille, name="marseille"),
    path("history/1885/", views.france_1885, name="france_1885"),
    path("history/1914/", views.france_1914, name="france_1914"),
    path("cities/paris/1924/", views.cities_paris_1924, name="cities_paris_1924"),

    # path("cities/<str:city>/<int:year>/", views.city_view, name="city_view"),
    re_path(r"^cities/(?P<city>\D+)/(?P<year>\d+)", views.city_view, name="city_view"),
    
    path(
        "cities/marseille/1956/",
        views.cities_marseille_1956,
        name="cities_marseille_1956",
    ),
]

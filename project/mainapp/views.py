from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, HttpResponseRedirect


# Create your views here.


def index_cite(request):
    return render(request, "index.html", {"greeting": "Города Франции"})


def history(request):
    return render(request, "history.html", {"greeting": "История"})


def history_info(request, age):
    ages = {
        1885: "Что происходило во Франции в 1885 году",
        1914: "Что происходило во Франции в 1914 году",
        1900: "Что происходило во Франции в 1900 году"
    }

    if age in ages:
        return render(request, "1885.html", {"greeting": ages[age][:]})

    else:
        return redirect("history")


def cities(request):
    return render(request, "cities.html", {"greeting": "Города"})


def facts(request):
    return render(request, "facts.html", {"greeting": "Факты о стране"})


def city_info(request, city):
    cities = {
        "paris": "Информация о Париже",
        "marseille": "Информация о Марселе",
    }
    if city in cities:
        return render(request, "paris.html", {"greeting": cities[city][:]})

    else:
        return redirect("cities")


def city_year(request, city, year):

    cities = {
        "paris": "Информация о Париже",
        "marseille": "Информация о Марселе",
    }

    dates = {
        1956: "Что происходило в Марселе в 1956 году",
        1924: "Что происходило в Париже в 1924 году",
    }


    if city in cities and year in dates:
        return render(request, "1956.html", {"greeting": dates[year][:]})
    else:
        return redirect("cities")


def paris(request):
    return render(request, "paris.html", {"greeting": "Информация о Париже"})


def marseille(request):
    return render(request, "marseille.html", {"greeting": "Информация о Марселе"})


def france_1885(request):
    return render(request, "1885.html", {"greeting": "Франция в 1885 году"})


def france_1914(request):
    return render(request, "1914.html", {"greeting": "Франция в 1914 году"})

def cities_paris_1924(request):
    
    return render(request, "1924.html", {"greeting": "Что происходило в Париже в 1924 году"})


def cities_marseille_1956(request):
    return render(
        request, "1956.html", {"greeting": "Что происходило в Марселе в 1956 году"}
    )

# Что то пошло не так, перенаправление на города???
def city_view(request, city="Undefined", year=0):
    city_query = f"city={city}&year={year}"

    if HttpResponse(city_query) == "city=Paris&year=1924":
        return redirect("cities/paris/1924/")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена, ошибка 404</h1>")

from django.shortcuts import render

from search.models import Country, Airport, Tour


def index(req):
    countries = Country.objects.all()
    departures = Airport.objects.all()
    return render(req, 'index.html', {"countries": countries, "departures": departures})


def search(req):
    countries = Country.objects.all()
    departures = Airport.objects.all()
    if req.method == 'GET':
        where_go = req.GET["where_go"]
        count_travelers = req.GET["travelers"]
        departure_from = req.GET["departure_from"]
        departure_id = Airport.objects.get(code=departure_from)
        country_id = Country.objects.get(name__contains=where_go)
        if departure_id and country_id:
            tours = Tour.objects.filter(departure=departure_id, count_travelers=count_travelers, hotel__city__country=country_id).order_by('-departure_date')
            return render(req, 'results.html', {"results": tours, "count": tours.count(), "countries": countries, "departures": departures})

from django.shortcuts import render, redirect

from search.models import Country, Airport, Tour, Request


def index(req):
    countries = Country.objects.all()
    departures = Airport.objects.all()
    partner_tours = Tour.objects.filter(promoted=True).order_by('departure_date')[:6]
    return render(req, 'index.html', {"countries": countries, "departures": departures, "tours": partner_tours})


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
            tours = Tour.objects.filter(departure=departure_id, count_travelers=count_travelers,
                                        hotel__city__country=country_id).order_by('departure_date')
            return render(req, 'results.html',
                          {"results": tours, "count": tours.count(), "countries": countries, "departures": departures})


def tour(req, id):
    countries = Country.objects.all()
    departures = Airport.objects.all()
    data = Tour.objects.get(id=id)
    if data:
        return render(req, 'tour.html', {"data": data, "countries": countries, "departures": departures})
    else:
        return redirect('index')


def request_form(req):
    if req.method == 'POST':
        form = Request(phone=req.POST["contact_phone"], email=req.POST["contact_email"], tour_id=req.POST["tour_id"])
        form.save()
        request_id = Request.objects.get(phone=req.POST["contact_phone"], email=req.POST["contact_email"], tour_id=req.POST["tour_id"])
        tour_obj = Tour.objects.get(id=req.POST["tour_id"])
        return render(req, 'success.html', {"data": tour_obj, "id": request_id.id})
    else:
        return redirect('index')


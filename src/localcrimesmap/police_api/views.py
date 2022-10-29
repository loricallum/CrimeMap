from django.shortcuts import render
import datetime
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from police_api.police_api_service import get_all_crimes,get_crimes_within_area, save_crimes_JSON

def get_all_crimes_api(request):
    if request.method == "GET":
        lat = request.GET['lat']
        lng = request.GET['lng']
        date = request.GET['date']
        crimesJSON = get_all_crimes(lat, lng, date)
        return JsonResponse(crimesJSON, safe=False)

    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def get_crimes_within_area_api(request):
    if request.method == "GET":
        polyArea = request.GET['area']
        date = request.GET['date']
        crimesJSON = get_crimes_within_area(polyArea, date)
        return JsonResponse(crimesJSON, safe=False)

    else:
        return HttpResponseNotFound('<h1> Page not found </h1>')
from django.shortcuts import render, HttpResponse
from applestore.apiservice import ApiService

def home(request):
    return HttpResponse('Hello World.')

def api(request):
    apiService = ApiService('AppleStore.csv', 'Reports.csv')
    response = apiService.consumer()
    return HttpResponse(response, content_type='application/json')

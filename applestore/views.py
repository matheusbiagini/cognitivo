from django.shortcuts import render, HttpResponse
from applestore.apiservice import ApiService

def home(request):
    return HttpResponse('Bem vindo ao meu teste para a empresa Cognitivo.')

def api(request):
    apiService = ApiService('AppleStore.csv', 'Reports.csv')
    response = apiService.consumer()
    return HttpResponse(response, content_type='application/json')

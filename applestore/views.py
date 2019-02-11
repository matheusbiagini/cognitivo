"""Return the HttpResponse and ApiService."""
from django.shortcuts import HttpResponse
from applestore.apiservice import ApiService
from applestore.applicationservice import ApplicationService
from applestore.csvservice import CsvService


def home(request):
    """Return the HttpResponse."""
    return HttpResponse('Bem vindo ao meu teste para a empresa Cognitivo.')


def api(request):
    """Consume api of applestore."""
    apiService = ApiService(
        'AppleStore.csv',
        ApplicationService(),
        CsvService(),
        'Reports.csv'
    )
    response = apiService.consumer()
    return HttpResponse(response, content_type='application/json')

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
    api_service = ApiService(
        csv_apple_store='AppleStore.csv',
        application_service=ApplicationService(),
        csv_service=CsvService(),
        reports_file='Reports.csv'
    )
    response = api_service.consumer()
    return HttpResponse(response, content_type='application/json')

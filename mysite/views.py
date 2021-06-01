#I have created this file-Nitin
from django.http import HttpResponse
def index(request):
    return HttpResponse("This is Home Page")

def about(request):
    return HttpResponse("This is About us Page")

def services(request):
    return HttpResponse("This is Services Page")

def contact(request):
    return HttpResponse("This is Contact us Page")
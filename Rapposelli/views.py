from django.http import HttpResponse


def index(request):
    return HttpResponse("CSC 230 Week 11")
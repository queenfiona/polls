"""pollsapp views."""
# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """Index function."""
    return HttpResponse("Hello world. Pollsapp views.")

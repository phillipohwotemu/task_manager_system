from django.shortcuts import render
from django.http import HttpResponse

# Example view
def dashboard(request):
    return HttpResponse("Welcome to the Dashboard")


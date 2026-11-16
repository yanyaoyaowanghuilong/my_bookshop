from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
# 视图层
def index(request):
    return HttpResponse("Book OK")
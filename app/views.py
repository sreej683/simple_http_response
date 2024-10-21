from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def telugu(request):
    return HttpResponse('this is our telugu movie')



def hindi(request):
    return HttpResponse('this is our hindi movie')
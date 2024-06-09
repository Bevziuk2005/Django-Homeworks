from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def simple_text(request):
    context = {
        'text': "Hello Word ! Python"
    }
    return render(request, 'notes/first.html', context)
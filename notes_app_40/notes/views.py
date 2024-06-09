from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Note

def simple_text(request):
    notes = Note.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'notes/first.html', context)
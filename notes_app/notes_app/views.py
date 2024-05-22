from django.http import HttpResponse

def simple_text(request):
    return HttpResponse("Hello from Notes app.")
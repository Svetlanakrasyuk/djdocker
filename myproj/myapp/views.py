from django.http import HttpResponse
from . import tasks

def home(request):
    tasks.mytask.delay()
    return HttpResponse('Hi world!')

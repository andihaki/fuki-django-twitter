from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

from .models import Tweet

# Create your views here.
def index(request):
    response = {
        'event': 'workshop-django',
        'time': datetime.now(),
    }
    return render(request, 'index.html', response)

def tweets(request):
    context = {
        'tweets': Tweet.objects.order_by('-created_at').all(),
    }
    return render(request, 'tweets.html', context)

def create(request):
    text = request.POST.get('tweet')
    Tweet.objects.create(text=text)
    return HttpResponseRedirect('/tweets/')
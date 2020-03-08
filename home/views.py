from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    topics = {'Coding', 'Developing', 'Movies', 'Web', 'ML', "AI", 'Flutter', 'Android' }
    creators = {'Derek_Banas', 'Coding_Cafe', 'Sim_Coder', 'Telusko'}
    return render(request, 'home_page.html', { "topics" : topics, "first_four_creators" : creators, 'next_four_creators' : creators })

def topic_detail(request):
    return render(request, 'topic_details.html', {})

def creater_detail(request):
    return render(request, 'creater_details.html', {})
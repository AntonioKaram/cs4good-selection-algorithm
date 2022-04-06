from django.shortcuts import render
from django.http import HttpResponse
from .funcs import readProjects, findMatches, makeRankings

# Create your views here.

def index(request):
    projects = makeRankings()
    # return render(request, 'stats/base.html')
    return render(request, 'stats/index.html', { 'projects': projects })


def upload(request):
    if request.method == "POST":
        print(request.FILES)
        projects = request.FILES['projects']
        people = request.FILES['people']

        with open('projects.csv', 'wb') as file:
            for chunk in projects.chunks():
                file.write(chunk)

        with open('people.csv', 'wb') as file:
            for chunk in people.chunks():
                file.write(chunk)

        return HttpResponse("recieved")

    return render(request, 'stats/upload.html')

from django.shortcuts import render

tasks = ['Lavar a louça', 'Tirar roupa do varal', 'Jogar videogame']

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })


def add(request):
    return render(request, "tasks/add.html")
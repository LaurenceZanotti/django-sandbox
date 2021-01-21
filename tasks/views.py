from django.shortcuts import render, redirect

tasks = []

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })


def add(request):
    if request.method == 'POST':
        new_task = request.POST['new-task']
        if not new_task:
            return render(request, "tasks/add.html")
        tasks.append(new_task)
        return redirect("/tasks") # Must use an url parser since hard coding url is bad practice
        
    return render(request, "tasks/add.html")
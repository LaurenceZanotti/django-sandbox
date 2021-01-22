from django.shortcuts import render, redirect
from django import forms

tasks = []

class NewTaskForm(forms.Form):
    """
    • Labels are put on by default and named after the variable name (in this case, new_task will be parsed as "New task:", if set to True)

    • To specify attributes, we need to add a widget as below (the details of why it is implemented this way is yet unknown to me).

    """
    new_task = forms.CharField(label=False, widget=forms.TextInput(attrs={"class": "form-control mt-1", "style": "width: 35%"}), required=True)
    """
    • In order to use min_value and max_value (and potentially other tools for validation) while using a widget (like 
    in this case, for CSS class), you must match the type of the widget and the type of field (e.g. IntegerField/NumberInput,
    and in other cases, probably CharField/TextInput). min and max_value didn't work when those weren't matched.

    • Multiple attrs (attributes) can be placed in dictionary format. In the first field I decided to use inline-css, while the second
    field I opted to use the class "input-width", which was written in the style tag in the template file.

    """
    priority = forms.IntegerField(min_value=0, max_value=10, widget=forms.NumberInput(attrs={"class": "form-control input-width mt-1"}))


# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })


def add(request):
    if request.method == 'POST':
        new_task = request.POST['new_task']
        if not new_task:
            return render(request, "tasks/add.html")
        tasks.append(new_task)
        return redirect("/tasks") # Must use an url parser since hard coding url is bad practice
        
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
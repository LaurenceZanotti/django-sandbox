from django.shortcuts import render, redirect
from django.urls import reverse
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
    in this case, for a CSS class), you must match the type of the widget and the type of field (e.g. IntegerField/NumberInput,
    and in other cases, probably CharField/TextInput). min and max_value didn't work when those fields weren't matched.

    • Multiple attrs (attributes) can be placed in a dictionary format. In the first field I decided to use inline-css, while the second
    field I opted to use the class "input-width", which was written in the te mplate file style tag.

    """
    # priority = forms.IntegerField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={"class": "form-control input-width mt-1"}))


# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })


def add(request):
    # If the route receives a post request
    if request.method == 'POST':
        # Store form fields as Django form
        form = NewTaskForm(request.POST)
        # Use Django built-in form validation
        if form.is_valid():
            task = form.cleaned_data["new_task"]
            tasks.append(task)
            return redirect(reverse("tasks:index")) # Do a "reverse engineer" to find where the url from tasks:index is
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
        
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
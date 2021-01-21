from django.shortcuts import render
from pyluach import dates

# Create your views here.
def index(request):
    # Jesus Christ Celebration at day 14th, Nissan (when he died)
    celebrationDate = dates.HebrewDate(
        dates.HebrewDate.today().year,
        1,
        14
    )

    # Check if current date is celebration date
    isCeleb = None
    if celebrationDate.to_jd == dates.GregorianDate.today().to_jd:
        isCeleb = True
    else:
        isCeleb = False

    return render(request, "celebration/index.html", {
        "date": celebrationDate.to_greg,
        "isCeleb": isCeleb
    })
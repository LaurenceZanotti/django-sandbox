from django.shortcuts import render
from pyluach import dates

# Create your views here.
def index(request):
    # Jesus Christ Celebration at day 14th, Nisan (when he died)
    celebrationDate = dates.HebrewDate(
        dates.HebrewDate.today().year,
        1,
        14
    )

    return render(request, "celebration/index.html", {
        "date": celebrationDate.to_greg,
        "isCeleb": celebrationDate.to_jd == dates.GregorianDate.today().to_jd
    })
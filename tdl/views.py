from django.shortcuts import render
from datetime import date

# Create your views here.

def index(request):

    today = date.today()

    context = {
        "today": today,
    }
    return render(request, "tdl/index.html", context)


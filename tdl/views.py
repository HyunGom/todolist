from django.shortcuts import render, redirect
from datetime import date
from .models import Task

# Create your views here.


def index(request):
    today = date.today()
    tasks = Task.objects.all()
    if request.method == "POST":
        task = Task(title=request.POST["title"])
        task.save()

        return redirect("index")

    context = {
        "today": today,
        "tasks": tasks,
    }

    return render(request, "tdl/index.html", context)


def complete(request, pk):
    task = Task.objects.get(id=pk)
    if task.complete:
        task.complete = False
    else:
        task.complete = True
    task.save()

    return redirect("index")


def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return redirect("index")

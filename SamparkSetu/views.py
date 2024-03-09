from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods

from .models import Todo

def about(request):
    return render(request,'about.html')

def home(request):
    todos = Todo.objects.all()
    return render(request, "home.html", {"todo_list": todos})


@require_http_methods(["POST"])
def add(request):
    # if request.method == "POST":
    title = request.POST["title"]
    todo = Todo(title=title)
    todo.save()
    return redirect("index")


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("index")


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")

def form(request):
    return render(request,'form.html')
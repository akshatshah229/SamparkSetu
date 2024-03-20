from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView
from .models import *
from .forms import *

from .models import Todo

def contactus(request):
    return render(request,'contactus.html')

def home(request):
    todos = Todo.objects.all()
    return render(request, "home.html", {"todo_list": todos})

def adminuser(request):
    return render(request, "adminuser.html")
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

# def form(request):
#     return render(request,'form.html')

class FormViewsModel(CreateView):
    model = FormModel
    form_class = FormViewsModel
    template_name = 'form.html'
    # fields = '__all__'
    success_url = reverse_lazy('form')

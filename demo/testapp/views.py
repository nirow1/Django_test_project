from django.shortcuts import render, HttpResponse, redirect
from .models import TodoList

def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, "home_page.html")

def todos(request):
    items = TodoList.objects.all()
    return render(request, "todos.html", {"todos": items})

def add_todo_item(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        completed = request.POST.get('completed') == "on"
        TodoList.objects.create(title=title, completed=completed)
        return redirect('todos')
    return render(request, "add_todo_item.html")
from datetime import datetime

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.utils.timezone import make_aware

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
        completed = False
        deadline = request.POST.get('deadline')
        if deadline:
            naive_deadline = datetime.strptime(deadline, "%Y-%m-%dT%H:%M")
            aware_deadline = make_aware(naive_deadline)
        else:
            aware_deadline = None
        TodoList.objects.create(title=title, completed=completed, deadline_day=aware_deadline)
        return redirect('todos')

    return render(request, "add_todo_item.html")

def delete_todo_item(request, todo_id):
    if request.method == "POST":
        todo = get_object_or_404(TodoList, id=todo_id)
        todo.delete()
        return redirect("todos")

def change_state(request, todo_id):
    if request.method == "POST":
        todo: TodoList= get_object_or_404(TodoList, id=todo_id)
        todo.completed = True
        todo.save()
        return redirect(todos)
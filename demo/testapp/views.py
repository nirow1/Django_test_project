from datetime import datetime

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.utils.timezone import make_aware

from .models import TodoList, ShoppingList, Item

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

def update_todo_item(request, todo_id):
    todo: TodoList = get_object_or_404(TodoList, id=todo_id)
    if request.method == "POST":
        todo.title = request.POST.get('title', todo.title)
        todo.completed = request.POST.get('completed', todo.completed) == "on"
        todo.deadline_day = request.POST.get('deadline_day', todo.deadline_day)
        todo.save()
        return redirect('todos')
    return render(request, 'update_todo.html', {'todo': todo})

def change_state(request, todo_id):
    if request.method == "POST":
        todo: TodoList= get_object_or_404(TodoList, id=todo_id)
        todo.completed = not todo.completed
        todo.save()
        return redirect(todos)

def add_shopping_list(request):
    if request.method == "POST":
        shopping_list_name = request.POST.get('list-name',
                                              'Unnamed List')
        shopping_list = ShoppingList.objects.create(name=shopping_list_name)
        
        # Get all information of the items from the form
        item_names = request.POST.getlist('name')
        item_quantities = request.POST.getlist('quantity')
        item_units = request.POST.getlist('unit')

        for item in item_names:
            if item.strip():  
                Item.objects.create(name=item.strip(), shopping_list=shopping_list)

        return redirect('/home_page')

    return render(request, 'add_shopping_list.html')

def shopping_lists(request):
    shopping_lists = ShoppingList.objects.prefetch_related('items').all()
    for list in shopping_lists:
        pass
    return render(request, 'shopping_lists.html', {'shopping_lists': shopping_lists})
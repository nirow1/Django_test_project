from datetime import datetime
from typing import List

from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import make_aware
from django.contrib.auth import authenticate, login, logout

from .models import TodoList, ShoppingList, Item

def base(request):
    return render(request, "base.html")

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('Home page')
        else:
            return redirect('Home page')
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

        for name, quantity, unit in zip(item_names, item_quantities, item_units):
            Item.objects.create(
                shopping_list=shopping_list,
                name=name,
                quantity=int(quantity),
                unit=unit
            )

        return redirect('/home_page')

    return render(request, 'add_shopping_list.html')

def delete_shopping_list(request, list_id):
    if request.method == "POST":
        shopping_list = get_object_or_404(ShoppingList, id=list_id)
        shopping_list.delete()
        return redirect("shopping_lists")
    
def update_shopping_list(request, list_id):
    shopping_list: ShoppingList = get_object_or_404(ShoppingList, id=list_id)
    items: List[Item] = shopping_list.items.all()

    if request.method == "POST":
        shopping_list.name = request.POST.get("list-name")
        shopping_list.save()

        item_names = request.POST.getlist('name')
        item_quantities = request.POST.getlist('quantity')
        item_units = request.POST.getlist('unit') 
        item_ids = request.POST.getlist('item_id')
        print(item_ids)
        for i in range(len(item_names)):
            try:
                if item_ids[i]:
                    item =  Item.objects.get(id = item_ids[i])
                    item.name = item_names[i]
                    item.quantity = int(item_quantities[i])
                    item.unit = item_units[i]
                    item.save()
            except:
                Item.objects.create(
                    shopping_list = shopping_list,
                    name = item_names[i],
                    quantity = int(item_quantities[i]),
                    unit = item_units[i],
                )   

        return redirect("shopping_lists")
    return render(request, 'update_shopping_list.html', {'shopping_list': shopping_list, "items": items})

def shopping_lists(request):
    shopping_lists = ShoppingList.objects.prefetch_related('items').all()
    for list in shopping_lists:
        pass
    return render(request, 'shopping_lists.html', {'shopping_lists': shopping_lists})

def logout_user(request):
    logout(request)
    return redirect('/home_page')
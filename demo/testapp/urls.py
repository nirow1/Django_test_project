from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="Base"),
    path("todos/", views.todos, name="todos"),
    path("home_page/", views.home, name="Home page"),
    path("add_todo_item/",  views.add_todo_item, name="add_todo_item"),
    path('delete/<int:todo_id>/', views.delete_todo_item, name='delete_todo_item'),
    path('change_state/<int:todo_id>/', views.change_state, name='change_state'),
    path('update_todo/<int:todo_id>/', views.update_todo_item, name='update_todo_item'),
]
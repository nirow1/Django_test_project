from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="Base"),
    path("todos/", views.todos, name="todos"),
    path("shopping_lists/", views.shopping_lists, name="shopping_lists"),
    path("home_page/", views.home, name="Home page"),

    path("add_todo_item/",  views.add_todo_item, name="add_todo_item"),
    path('delete/<int:todo_id>/', views.delete_todo_item, name='delete_todo_item'),
    path('update_todo/<int:todo_id>/', views.update_todo_item, name='update_todo_item'),
    path('change_state/<int:todo_id>/', views.change_state, name='change_state'),

    path("add_shopping_list/", views.add_shopping_list, name="add_shopping_list"),
    path('delete_list/<int:list_id>/', views.delete_shopping_list, name='delete_shopping_list'),
    path('update_list/<int:list_id>/', views.update_shopping_list, name='update_shopping_list'),

    path('logout/', views.logout_user, name='logout'),
]
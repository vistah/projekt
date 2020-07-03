from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # urls for the first semester
    path('first_semester.html', views.first, name='first'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall'),
    path('delete/<todo_id>', views.deleteTodo, name="delete"),

    # urls for the second semester
    path('second_semester.html', views.second, name="second"),
    path('add_second', views.addTodoSecond, name='add-second'),
    path('complete-second/<todo_id>', views.completeTodoSecond, name='complete-second'),
    path('deletecomplete_second', views.deleteCompletedSecond, name='deletecomplete-second'),
    path('deleteall-second', views.deleteAllSecond, name='deleteall-second'),
    path('delete-second/<todo_id>', views.deleteTodoSecond, name="delete-second"),

]

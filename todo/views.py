from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .models import Todo
from .forms import TodoForm


#view for the link index.html
def index(request):
    return render(request, 'todo/index.html')


#views for the link first_semester.html
def first(request):
    todo_list = Todo.objects.all().filter(semester=1).order_by('id')

    form = TodoForm()

    context = {'todo_list': todo_list, 'form': form}

    return render(request, 'todo/first_semester.html', context)


#views for the link second_semester.html
def second(request):
    todo_list = Todo.objects.all().filter(semester=2).order_by('id')

    form = TodoForm()

    context = {'todo_list': todo_list, 'form': form}

    return render(request, 'todo/second_semester.html', context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        #new_todo = form.save(commit=False)
        new_todo.save()

    return redirect('first')


@require_POST
def addTodoSecond(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.semester=2
        new_todo.save()

    return redirect('second')


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('first')


def completeTodoSecond(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('second')


def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('first')


def deleteCompletedSecond(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('second')


def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('first')


def deleteAllSecond(request):
    Todo.objects.all().delete()

    return redirect('second')


@csrf_exempt
def deleteTodo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/first_semester.html')


@csrf_exempt
def deleteTodoSecond(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/second_semester.html')


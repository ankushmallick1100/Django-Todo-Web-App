from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Todo

# Create your views here.
def list_todo_items(request):
    todo_list = Todo.objects.all()
    return render(request, 'todos/todo_list.html', locals())

def insert_todo_item(request:HttpRequest):
    content = request.POST['content']
    if(content == ''):
        return redirect('/todos/list/')
    Todo(content=content).save()
    return redirect('/todos/list/')

def delete_todo_item(request, todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/')

def update_todo_item(request, todo_id):
    todo_to_update = Todo.objects.get(id=todo_id)
    todoContent = todo_to_update.content
    todoId = todo_id
    return render(request, 'todos/todo_edit.html', locals())

def update(request:HttpRequest, todoId):
    todoId = int(todoId)
    content = request.POST['content']
    todoUpdate = Todo.objects.get(id=todoId)
    todoUpdate.content = content
    todoUpdate.save()
    return redirect("/todos/list/")
    
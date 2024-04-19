from django.shortcuts import render, redirect
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todolist/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        todo_text = request.POST.get('todo', '')
        todo_content = request.POST.get('content', '')
        if todo_text:
            Todo.objects.create(todo=todo_text, content=todo_content)
            return redirect('todo_list')
    return render(request, 'todolist/add_todo.html')

def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.completed = not todo.completed  # Toggle the completed status
        todo.save()
        return redirect('todo_list')
    return render(request, 'todolist/todo_list.html', {'todo': todo})

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')
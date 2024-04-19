from django.shortcuts import render, redirect
from .models import Todo

def todo_list(request):
    # 모든 할 일을 가져와서 todo_list.html 템플릿에 전달하는 뷰 함수
    todos = Todo.objects.all()
    return render(request, 'todolist/todo_list.html', {'todos': todos})

def add_todo(request):
    # 할 일을 추가하는 뷰 함수
    if request.method == 'POST':
        # POST 요청을 받으면 사용자로부터 입력 받은 할 일과 내용을 가져와서 데이터베이스에 저장하고 todo_list 페이지로 리디렉션
        todo_text = request.POST.get('todo', '')  # 할 일
        todo_content = request.POST.get('content', '')  # 내용
        if todo_text:  # 할 일이 비어있지 않으면
            Todo.objects.create(todo=todo_text, content=todo_content)  # 데이터베이스에 할 일 추가
            return redirect('todo_list')  # todo_list 페이지로 리디렉션
    # GET 요청이거나 할 일이 비어있는 경우에는 할 일을 추가하는 페이지를 보여줌
    return render(request, 'todolist/add_todo.html')

def complete_todo(request, todo_id):
    # 할 일을 완료 상태로 변경하는 뷰 함수
    todo = Todo.objects.get(id=todo_id)  # 해당 ID의 할 일을 가져옴
    if request.method == 'POST':
        # POST 요청을 받으면 해당 할 일의 완료 상태를 반전시키고 데이터베이스에 저장한 뒤 todo_list 페이지로 리디렉션
        todo.completed = not todo.completed  # 완료 상태 반전
        todo.save()  # 변경 사항 저장
        return redirect('todo_list')  # todo_list 페이지로 리디렉션
    # GET 요청인 경우에는 해당 할 일을 완료 상태로 변경하는 페이지를 보여줌
    return render(request, 'todolist/todo_list.html', {'todo': todo})

def delete_todo(request, todo_id):
    # 할 일을 삭제하는 뷰 함수
    todo = Todo.objects.get(id=todo_id)  # 해당 ID의 할 일을 가져옴
    todo.delete()  # 할 일 삭제
    return redirect('todo_list')  # todo_list 페이지로 리디렉션


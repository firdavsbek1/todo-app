from django.shortcuts import render,redirect
from .models import Todo
from datetime import datetime

date_now=datetime.now().strftime("%Y-%m-%dT%H:%M")


def main_page(request):
    todo_list=Todo.objects.all()
    if request.method=="POST":
        try:
            todo_text = request.POST.get("todo-text")
            due_date=datetime.strptime(request.POST.get("due-date"),"%Y-%m-%dT%H:%M")
        except ValueError:
            due_date=date_now
        finally:
            if todo_text:
                todo = Todo.objects.create(todo_text=todo_text, due_date=due_date)
    return render(request,"todo_list.html",context={"todo_list":todo_list,"date_now":date_now})


def edit_todo(request,pk):
    todo=Todo.objects.get(pk=pk)
    due_date_formatted=todo.due_date.strftime("%Y-%m-%dT%H:%M")
    if request.method=="POST":
        todo_text = request.POST.get("todo-text")
        due_date = datetime.strptime(request.POST.get("due-date"), "%Y-%m-%dT%H:%M")
        if todo_text:
            todo.todo_text = todo_text
            todo.due_date = due_date
            todo.created=datetime.now()
            todo.save()
        return redirect("main-page")
    return render(request,'edit.html',context={"todo":todo,"due_date_formatted":due_date_formatted})


def delete_todo(request,pk):
    todo = Todo.objects.get(id=pk)
    if request.method=="POST":
        todo.delete()
        return redirect('main-page')
    return render(request,'delete.html',context={"todo":todo})


def check_todo(request,pk):
    todo = Todo.objects.get(pk=pk)
    todo.done=True
    todo.save()
    return redirect("main-page")


def uncheck_todo(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.done=False
    todo.save()
    return redirect("main-page")

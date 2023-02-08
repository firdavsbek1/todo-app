from django.contrib.auth.forms import User
from django.shortcuts import render,redirect
from .models import Todo
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm

date_now=datetime.now().strftime("%Y-%m-%dT%H:%M")


def main_page(request):
    try:
        todo_list = request.user.todo_set.all()
    except:
        todo_list=None
    if request.method=="POST":
        if request.user.is_authenticated:
            try:
                todo_text = request.POST.get("todo-text")
                due_date=datetime.strptime(request.POST.get("due-date"),"%Y-%m-%dT%H:%M")
            except ValueError:
                due_date=date_now
            finally:
                if todo_text:
                    todo = Todo.objects.create(owner=request.user,todo_text=todo_text, due_date=due_date)
        else:
            return redirect('login')
    return render(request,"todo_list.html",context={"todo_list":todo_list,"date_now":date_now})


@login_required(login_url='login')
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


@login_required(login_url='login')
def delete_todo(request,pk):
    todo = Todo.objects.get(id=pk)
    if request.method=="POST":
        todo.delete()
        return redirect('main-page')
    return render(request,'delete.html',context={"todo":todo})


@login_required(login_url='login')
def check_todo(request,pk):
    todo = Todo.objects.get(pk=pk)
    todo.done=True
    todo.save()
    return redirect("main-page")


@login_required(login_url='login')
def uncheck_todo(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.done=False
    todo.save()
    return redirect("main-page")


def register_user(request):
    form=SignupForm()
    if request.method=="POST":
        try:
            user=User.objects.get(username=request.POST.get('username'))
            messages.error(request,"User with that username already exists!Try again!")
            return redirect('register')
        except:
            form = SignupForm(request.POST)
            form.save()

        return redirect('login')
    return render(request,"registration/register.html",context={"form":form})


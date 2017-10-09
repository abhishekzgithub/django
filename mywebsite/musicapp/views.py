from django.shortcuts import render, redirect
from django.http import request, response, HttpResponse
from .models import Todo

# Create your views here.
def index(request):
    todos=Todo.objects.all()[:10]
    context = {
        'todos':todos
    }
    return render(request, 'index.html',context)

def details(request,id):
    todo_details=Todo.objects.get(id=id)
    context={
        'todo_details':todo_details,
    }
    return render(request,'details.html',context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todos/index')
    else:
        return render(request, 'add.html')

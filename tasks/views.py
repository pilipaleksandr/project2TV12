from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'tasks/task_add.html')

def task_complete(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('task_list')

def task_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('task_list')

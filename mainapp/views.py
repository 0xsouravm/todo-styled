from django.shortcuts import render,redirect
from .models import Task

def showlist(request):
    tasks = Task.objects.all()
    task_list = {
        'task_list': tasks[::-1]
    }
    return render(request,'mainapp/main.html', context = task_list)

def addtask(request):
    if request.method == 'POST':
        task_added = request.POST['task_added']
        if task_added!='':
            Task(task=task_added).save()
    return redirect('showlist')

def removetask(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('showlist')

def finishtoggle(request,id):
    task = Task.objects.get(id=id)
    if task.is_complete == True:
        task.is_complete = False
    else:
        task.is_complete = True
    task.save()
    return redirect('showlist')

def modifytask(request,id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        new_task = request.POST['modified']
    task.task = new_task
    task.is_complete = False
    task.save()
    return redirect('showlist')
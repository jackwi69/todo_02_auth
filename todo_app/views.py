from django.shortcuts import render, get_object_or_404, redirect

from . models import Task
from . forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request, 'todo_app/index.html', context)


def detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'todo_app/detail.html', context)


def upgrade(request, pk):
    taskpk = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=taskpk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=taskpk)
        if form.is_valid():
            form.save()
            return redirect('todo_app:index')
    context = {'form': form}
    return render(request, 'todo_app/upgrade.html', context)


def create_task(request):
    form = TaskForm(request.POST)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_app:index')
    context = {'form':form}
    return render(request, 'todo_app/create.html', context)


from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .form import TaskForm
from .models import Task


def create_task(request):
    status_filter = request.GET.get('status', 'all')

    if status_filter == 'P':
        tasks = Task.objects.filter(status='P')
    elif status_filter == 'C':
        tasks = Task.objects.filter(status='C')
    else:
        tasks = Task.objects.all()

    if request.method == 'GET':
        context = {
            'form': TaskForm(),
            'task_list': tasks,
            'current_status': status_filter
        }
        return render(request, 'todo.html', context=context)

    elif request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('create_task')
        else:
            return HttpResponse('Error saving the task')


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)

    title = request.POST.get('task')
    deadline = request.POST.get('deadline')
    status = request.POST.get('status')

    task.task = title
    task.deadline = deadline
    task.status = status

    task.save()
    return redirect('create_task')


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('create_task')

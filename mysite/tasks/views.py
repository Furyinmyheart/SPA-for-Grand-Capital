from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def save_task_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            tasks = Task.objects.all()
            data['html_task_list'] = render_to_string('tasks/includes/partial_task_list.html', {
                'tasks': tasks
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
    else:
        form = TaskForm()
    return save_task_form(request, form, 'tasks/includes/partial_task_create.html')


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
    else:
        form = TaskForm(instance=task)
    return save_task_form(request, form, 'tasks/includes/partial_task_update.html')


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    data = dict()
    if request.method == 'POST':
        task.delete()
        data['form_is_valid'] = True
        tasks = Task.objects.all()
        data['html_task_list'] = render_to_string('tasks/includes/partial_task_list.html', {'tasks': tasks})
    else:
        context = {'task': task}
        data['html_form'] = render_to_string('tasks/includes/partial_task_delete.html', context, request=request)
    return JsonResponse(data)

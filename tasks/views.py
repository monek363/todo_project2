from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from users.views import login_required, get_current_user
from .models import Task
from .forms import TaskForm


# Create your views here.

def main(request):
    return render(request, "main.html")

@login_required
def index(request):
    user = get_current_user(request)

    tasks = Task.objects.all()


    do_tasks = tasks.filter(completed=False)
    done_tasks = tasks.filter(completed=True)

    context = {
        'user': user,
        'do_tasks': do_tasks,
        'done_tasks': done_tasks
    }
    return render(request, "index.html", context)

@login_required
def create_task(request):
    user = get_current_user(request)

    if request.method == 'POST':
        formsTaskForm(request.POST)
        if form.is_valid():
            rask = form.save()

            if request.headers.get('X-required-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'task': {
                        'id': task.id,
                        'title': task.title,
                        'description': task.description,
                        'priority': task.priority,
                        'complexity': task.get_complexity_display(),
                        'color': task.color,
                        'completed': task.completed
                    }
                    
                })
            return redirect('profile')
    else:
        form = TaskForm()
    context = {
        'user': user,
        'form': form,
    }            
    return render(request, "create_task.htm", context)

@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'completed': task.completed})
    return redirect('profile')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True})
    
    return redirect('profile')
    
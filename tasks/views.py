from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import models
from tasks.forms import TaskModelForm, TaskForm, TaskDetailsModelForm
from tasks.models import task as Task, taskdetails as TaskDetails, project as Project, employee as Employee
from django.contrib import messages



# Create your views here.
def manager_dashboard(request):
    type= request.GET.get('type','all')
    base_query= Task.objects.select_related('details').prefetch_related('assigned_to')

    #getting task count
    counts= Task.objects.aggregate(
        total_task= models.Count('id'),
        completed_task= models.Count('id', filter=models.Q(status='COMPLETED')),
        pending_task= models.Count('id', filter=models.Q(status='PENDING')),
        in_progress_task= models.Count('id', filter=models.Q(status='IN PROGRESS')),
    )

    #retrieving task based on type
    if type == 'completed':
        task= base_query.filter(status='COMPLETED')
    elif type == 'pending':
        task= base_query.filter(status='PENDING')
    elif type == 'in_progress':
        task= base_query.filter(status='IN PROGRESS')
    else:
        task= base_query.all()
    
    context= {
        'task': task,
        'counts': counts,
    }
    return render(request, "dashboard/manager-dashboard.html", context)

def user_dashboard(request):
    return render(request,"dashboard/user-dashboard.html")

def test_view(request):
    return render(request, "test.html")

def create_task(request):
    task_form= TaskModelForm()
    task_details_form= TaskDetailsModelForm()

    if request.method == 'POST':
        task_form= TaskModelForm(request.POST)
        task_details_form= TaskDetailsModelForm(request.POST)

        if task_form.is_valid() and task_details_form.is_valid():
            """using django ModelForm"""
            task=task_form.save()
            task_detail=task_details_form.save(commit=False)
            task_detail.task= task
            task_detail.save()

            messages.success(request, "Task created successfully!")
            return redirect('create-task')
    
    context = {'task_form': task_form, 'task_details_form': task_details_form}
    return render(request, "task_form.html", context)


def update_task(request ,id):
    task= Task.objects.get(id=id)
    task_form= TaskModelForm(instance=task)

    if task.details:
        task_details_form= TaskDetailsModelForm(instance=task.details)
        
    if request.method == 'POST':
        task_form= TaskModelForm(request.POST, instance=task)
        task_details_form= TaskDetailsModelForm(request.POST, instance=task.details)

        if task_form.is_valid() and task_details_form.is_valid():
            """using django ModelForm"""
            task=task_form.save()
            task_detail=task_details_form.save(commit=False)
            task_detail.task= task
            task_detail.save()

            messages.success(request, "Task  successfully!")
            return redirect('update-task',id=id)
    
    context = {'task_form': task_form, 'task_details_form': task_details_form}
    return render(request, "task_form.html", context)

def delete_task(request, id):
    if request.method == 'POST':
        task= Task.objects.get(id=id)
        task.delete()
        messages.success(request, "Task Deleted successfully!")
        return redirect('manager-dashboard')
    else:
        messages.error(request, "Invalid request method.")
        return redirect('manager-dashboard')
    
    



def view_task(request):
    # select related query(foreign key, one to one fields)
    task= Task.objects.select_related('details').all()
    return render(request, "show_task.html", {'task': task,})
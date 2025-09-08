from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskModelForm, TaskForm
from tasks.models import task as Task, taskdetails as TaskDetails, project as Project, employee as Employee
# Create your views here.
def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request,"dashboard/user-dashboard.html")

def test_view(request):
    return render(request, "test.html")

def create_task(request):
    form= TaskModelForm()

    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            """using django ModelForm"""
            form.save()
            return render(request, "task_form.html", {'form': form, 'message': "Task created successfully!"})
    
    context = {'form': form}
    return render(request, "task_form.html", context)

def view_task(request):
    # select related query(foreign key, one to one fields)
    task= Task.objects.select_related('details').all()
    return render(request, "show_task.html", {'task': task,})
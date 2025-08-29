from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskModelForm
from tasks.models import employee, task, taskdetails, project


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


            """" Using django Form data """
            # title = form.cleaned_data.get('title')
            # description = form.cleaned_data.get('description')
            # due_date = form.cleaned_data.get('due_date')
            # assigned_to_ids = form.cleaned_data.get('assigned_to')

            # # Create the task instance
            # new_task = task.objects.create(
            #     title=title,
            #     description=description,
            #     due_date=due_date
            # )

            # # Assign employees to the task
            # for emp_id in assigned_to_ids:
            #     employee_instance = employee.objects.get(id=emp_id)
            #     new_task.assigned_to.add(employee_instance)
            # new_task.save()
            # return HttpResponse("Task created successfully!")
    
    context = {'form': form}
    return render(request, "task_form.html", context)


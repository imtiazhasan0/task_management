from django.contrib import admin
from tasks.models import task, employee, project, taskdetails


# Register your models here.
admin.site.register(task)
admin.site.register(employee)
admin.site.register(project)
admin.site.register(taskdetails)
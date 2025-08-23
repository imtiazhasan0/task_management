from django.contrib import admin
from django.urls import path
from tasks.views import show_tasks
 


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('show_tasks/', show_tasks)
]
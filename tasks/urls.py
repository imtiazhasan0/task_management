from django.contrib import admin
from django.urls import path
from tasks.views import manager_dashboard,user_dashboard,test_view,create_task,view_task
 
urlpatterns = [
    path('manager-dashboard/', manager_dashboard),
    path('user-dashboard/', user_dashboard),
    path('test/', test_view),
    path('create-task/', create_task),
    path('view-task/', view_task),
]
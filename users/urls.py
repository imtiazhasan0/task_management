from django.contrib import admin
from django.urls import path
from users.views import people


urlpatterns = [
    path('admin/', admin.site.urls),
    path('people/', people)
]
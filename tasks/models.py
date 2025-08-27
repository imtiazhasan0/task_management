from django.db import models

# Create your models here.
class employee(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(unique=True)



class task(models.Model):
    project= models.ForeignKey('project', on_delete=models.CASCADE, default=1)
    assigned_to= models.ManyToManyField(employee)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class taskdetails(models.Model):
    HIGH, MEDIUM, LOW = 'H', 'M', 'L'
    PRIORITY=(
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low')
    )
    task = models.OneToOneField(task, on_delete=models.CASCADE,related_name='details')
    assigned_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY, default= 'L')

class project(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
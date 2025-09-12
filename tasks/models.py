from django.db import models

class employee(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(unique=True)
    def __str__(self):
        return self.name


class task(models.Model):
    status_choices = [
        ('PENDING', 'Pending'),
        ('IN PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]
    project= models.ForeignKey('project', on_delete=models.CASCADE, default=1)
    assigned_to= models.ManyToManyField(employee)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=status_choices, default='PENDING')
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class taskdetails(models.Model):
    HIGH, MEDIUM, LOW = 'H', 'M', 'L'
    PRIORITY=(
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low')
    )
    task = models.OneToOneField(task, on_delete=models.CASCADE,related_name='details')
    #assigned_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY, default= 'L')
    notes = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"Details of {self.task.title}"

class project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    def __str__(self):
        return self.name
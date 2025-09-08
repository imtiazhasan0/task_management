import os
import django
from faker import Faker
import random
from tasks.models import employee, project, task, taskdetails

#setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management.settings')
django.setup()

#function to populate the database
def populate_db(n_employees=10, n_projects=5, n_tasks=20):
    fake =Faker()

    # Create Employees
    employees = []
    for _ in range(n_employees):
        emp = employee.objects.create(
            name=fake.name(),
            email=fake.unique.email()
        )
        employees.append(emp)
    print(f"Created {n_employees} employees.")

    # Create Projects
    projects = []
    for _ in range(n_projects):
        proj = project.objects.create(
            name=fake.bs().title(),
            description=fake.text(max_nb_chars=200),
            start_date=fake.date_this_decade()
        )
        projects.append(proj)
    print(f"Created {n_projects} projects.")

    # Create Tasks
    for _ in range(n_tasks):
        proj = random.choice(projects)
        task_instance = task.objects.create(
            project=proj,
            title=fake.sentence(nb_words=6),
            description=fake.text(max_nb_chars=300),
            is_completed=random.choice([True, False]),
            status=random.choice(['PENDING', 'IN PROGRESS', 'COMPLETED']),
            due_date=fake.date_between(start_date='today', end_date='+30d')
        )
        assigned_employees = random.sample(employees, k=random.randint(1, 3))
        task_instance.assigned_to.set(assigned_employees)
        task_instance.save()
        print(f"Created task: {task_instance.title}")

        # Create Task Details
        task_detail = taskdetails.objects.create(
            task=task_instance,
            assigned_to=', '.join([emp.name for emp in assigned_employees]),
            priority=random.choice(['H', 'M', 'L']),
            notes=fake.text(max_nb_chars=100)
        )
        print(f"Created task details for: {task_detail.task.title}")
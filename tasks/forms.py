from django import forms
from tasks.models import employee, task, taskdetails, project

#django form for creating a new task
class TaskForm(forms.Form):
    title=forms.CharField(max_length=250)
    description=forms.CharField(widget=forms.Textarea)
    due_date=forms.DateField(widget=forms.SelectDateWidget)
    assigned_to=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,)


    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        employees = employee.objects.all()
        self.fields['assigned_to'].choices = [(emp.id, emp.name) for emp in employees]

#django Mixin form
# class styleMixin:
#     def add_style(self, *args):
#         for fieldname in args:
#             field = self.fields.get(fieldname)
#             if field:
#                 existing_classes = field.widget.attrs.get('class', '')
#                 field.widget.attrs['class'] = (existing_classes + ' ' if existing_classes else '') + 'border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'


#django model from
class TaskModelForm(forms.ModelForm):
    class Meta:
        model = task
        fields = ['title', 'description', 'due_date', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={
                'size': 40,
                'placeholder': 'Enter task title'
                }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'cols': 40,
                'placeholder': 'Enter task description'
                }),
            'due_date': forms.SelectDateWidget(),
            'assigned_to': forms.CheckboxSelectMultiple(),
        }
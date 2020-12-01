from django import forms 
from app_todolist.models import TaskList 

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList 
        fields = ['task', 'done']
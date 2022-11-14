import datetime

from django import forms

from todo.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        input_formats='%Y-%m-%d %H:%M',
        required=False,
        initial=datetime.datetime.today
    )

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")
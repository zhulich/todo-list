from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tag


# Create your views here.


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    queryset = Task.objects.all()


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("practice:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("practice:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("practice:task-list")


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("practice:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("practice:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("practice:tag-list")


def toggle_assign_to_task(request, pk):
    task = Task.objects.get(id=pk)
    if task.completed:
        task.completed = False
    else:
        task.completed = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("practice:task-list"))



from django.shortcuts import render
from django.views import generic

from core.models import Tag, Task


# Create your views here.


class TaskListView(generic.ListView):
    model = Task
    template_name = "core/index.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "core/tags.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = "/tags"




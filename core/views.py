

from django.shortcuts import render
from django.views import generic

from core.models import Tag


# Create your views here.


def index(request):
    return render(request, "core/index.html")


class TagListView(generic.ListView):
    model = Tag
    template_name = "core/tags.html"

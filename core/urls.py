from django.urls import path

from core.views import TagListView, TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("tags/", TagListView.as_view(), name="tags"),
]



app_name = "core"

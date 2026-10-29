from django.urls import path

from core.views import TagListView, TaskListView, TagCreateView, TagUpdateView, TagDeleteView, TaskCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tags/create/", TagCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tags-delete"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "core"

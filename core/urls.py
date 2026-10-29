from django.urls import path

from core.views import TagListView, TaskListView, TagCreateView, TagUpdateView, TagDeleteView, TaskCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "core"

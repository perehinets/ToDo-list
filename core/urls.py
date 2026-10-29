from django.urls import path

from core.views import index, TagListView

urlpatterns = [
    path("", index, name="home"),
    path("tags/", TagListView.as_view(), name="tags"),
]



app_name = "core"

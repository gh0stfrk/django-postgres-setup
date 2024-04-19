from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.hello_world, name="hello_world"),
    path("user/", views.create_user, name="create_user"),
]

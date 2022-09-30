from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("zibi", views.zibi, name="zibi"),
    path("mati", views.mati, name="zibi"),
    path("<str:name>", views.greet, name="greet")
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.rollout,name="rolloutchecks"),
]
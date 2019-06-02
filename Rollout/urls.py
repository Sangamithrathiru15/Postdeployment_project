from django.urls import path
from . import views

urlpatterns = [
    path('',views.rollout,name="rolloutchecks"),
    path('<int:store_num>/rolloutresult/',views.rolloutdisplay,name="rollout-display"),
]
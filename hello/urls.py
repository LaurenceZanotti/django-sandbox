from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('laurence/', views.laurence, name="laurence"),
    path('nadine/', views.nadine, name="nadine")
]

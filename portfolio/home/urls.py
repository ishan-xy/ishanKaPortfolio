from django.urls import include, path
from . import views 
from projects import views as projects_views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', projects_views.index , name='projects'),
]
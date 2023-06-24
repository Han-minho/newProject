from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path("",views.IndexView.as_view(),name='index'),
    path("",views.DetailView.as_view(),name='detail'),
    path("",views.vote.as_view(),name='vote'),
    path("",views.ResultView.as_view(),name='results')
]
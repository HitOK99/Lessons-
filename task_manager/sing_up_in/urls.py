from django.urls import path
from . import views

urlpatterns = [
    path('', views.sing_up_in, name='sing_up_in'),
    path('sing_in', views.sing_in, name='sing_in')
]

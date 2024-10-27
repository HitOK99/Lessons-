from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_work_window, name='main_work_window'),
    path('add_task/', views.add_task, name='add_task'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


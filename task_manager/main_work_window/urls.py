from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_task, name='add_task'),
    path('news', views.news, name='news'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('add_subtask/<int:task_id>/', views.add_subtask_view, name='add_subtask'),
    path('delete_subtask/<int:subtask_id>/', views.delete_subtask, name='delete_subtask'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

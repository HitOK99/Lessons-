from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('work_window', include('main_work_window.urls')),
    path('', include('sing_up_in.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

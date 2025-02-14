from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('start/', views.start_assistant, name='start_assistant'),
    path('', views.index, name='index'), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
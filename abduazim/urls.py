from django.urls import path
from .views import about, blog, project_detail, test
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", about, name="view"),
    path('blog/<int:pk>/', blog, name="blog-detail"),
    path('project/<int:pk>/',project_detail, name="project-detail"),
    path('test/', test, name= "test" )
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
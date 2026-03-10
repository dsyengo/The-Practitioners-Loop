from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import AdminLoginView, AdminLogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.health_check, name='health-check'),
    path('admin/', admin.site.urls),
    
    # Swagger Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # Auth endpoints
    path('dashboard/login/', AdminLoginView.as_view(), name='dashboard-login'),
    path('dashboard/logout/', AdminLogoutView.as_view(), name='dashboard-logout'),
    path('dashboard/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    
    # contact form api
    path('api/', include('contact.urls')),
    # blogs api
    path('api/blogs/', include('blogs.urls')),
    # projects api
    path('api/projects/', include('projects.urls')),
    # experience api
    path('api/experience/', include('experience.urls')),
    # certifications api
    path('api/certifications/', include('certifications.urls')),  
]

# This allows Django to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
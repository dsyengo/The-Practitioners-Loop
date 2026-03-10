from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DashboardCertificationViewSet, PublicCertificationViewSet

dashboard_router = DefaultRouter()
dashboard_router.register(r'items', DashboardCertificationViewSet, basename='dashboard-certs')

public_router = DefaultRouter()
public_router.register(r'items', PublicCertificationViewSet, basename='public-certs')

urlpatterns = [
    # Dashboard API (Protected) 
    path('dashboard/', include(dashboard_router.urls)),
    
    # Public API (Read-Only)
    path('public/', include(public_router.urls)),
]
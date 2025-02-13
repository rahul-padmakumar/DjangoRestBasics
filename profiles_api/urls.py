from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(prefix='view_set', viewset=views.HelloViewSet, basename="hello_view_set")

urlpatterns = [
    path('view', views.HelloApiView.as_view()),
    path('', include(router.urls))
]

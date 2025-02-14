from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(prefix='view_set', viewset=views.HelloViewSet, basename="hello_view_set")
router.register(prefix='profile', viewset=views.ProfileViewSet, basename="profile")

urlpatterns = [
    path('view', views.HelloApiView.as_view()),
    path('', include(router.urls)),
    path('login', views.LoginApiView.as_view())
]

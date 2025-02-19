from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(prefix='view_set', viewset=views.HelloViewSet, basename="hello_view_set")
router.register(prefix='profile', viewset=views.ProfileViewSet, basename="profile")
router.register('feed', viewset=views.ProfileFeedViewSet, basename="profile_feed")

urlpatterns = [
    path('view', views.HelloApiView.as_view()),
    path('', include(router.urls)),
    path('login', views.LoginApiView.as_view()),
    path('generic/create', views.CreateGenericView.as_view()),
    path('generic/retrieve/<pk>', views.RetrieveGenericView.as_view()),
    path('generic/update/<pk>', views.UpdateGenericView.as_view()),
    path('generic/delete/<pk>', views.DeleteGenericView.as_view()),
    path('generic/list_create', views.ListCreateGenericView.as_view()),
    path('generic/retrieve_update/<pk>', views.RetrieveUpdateView.as_view()),
    path('generic/retrieve_destroy/<pk>', views.RetrieveDestroyView.as_view()),
    path('generic/all/<pk>', views.RetrieveDestroyUpdateView.as_view())
]

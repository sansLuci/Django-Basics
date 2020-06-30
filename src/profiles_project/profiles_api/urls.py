from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewset, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet) #No need to use 'basename' as using ModelViewSet
router.register('login', views.LoginViewSet, basename='login')
router.register('feed',views.UserProfileFeedViewSet)
 
urlpatterns = [
	path('hello-view/', views.HelloAPIView.as_view()),
	path('', include(router.urls)),
]

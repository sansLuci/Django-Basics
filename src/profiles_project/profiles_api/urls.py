from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewset, basename='hello-viewset')

# urlpatterns = router.urls

# router = DefaultRouter('hello-viewset', views.HelloViewset, base_name='hello-viewset')
 
urlpatterns = [
	path('hello-view/', views.HelloAPIView.as_view()),
	path('', include(router.urls)),
]

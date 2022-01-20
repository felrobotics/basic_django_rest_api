from django.urls import path
# from rest_framework import routers
from django.urls import path, include

from basic_api import views

# for view set
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register('test-viewset', views.TestViewSet, basename='test-viewset')

urlpatterns = [
    path('test-apiview/', views.TestApiView.as_view()),
    path('', include(router.urls)), # first is blank to not put a prefix    
]
from django.urls import path

from basic_api import views



urlpatterns = [
    path('test-view/', views.TestApiView.as_view()),
]
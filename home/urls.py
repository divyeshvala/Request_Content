from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home_view'),
    path('topic_details/', views.topic_detail, name='topic_detail_view'),
    path('creator_details/', views.creater_detail ),
]
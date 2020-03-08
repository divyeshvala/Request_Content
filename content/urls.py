from django.urls import path
from . import views

urlpatterns = [
    path('ideas', views.display_ideas, name="display_ideas_view_url"),
    path('submit_idea', views.submit_idea, name="submit_idea_view_url"),
    path('topics', views.topics, name="topics_view_url"),
    path('creators', views.creators, name="creators_view_url"),
]

from django.urls import path
from .views import PlayListView

urlpatterns = [
    path('', PlayListView.as_view()),
]

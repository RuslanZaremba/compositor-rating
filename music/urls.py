from django.urls import path
from .views import PlayListView

urlpatterns = [
    path('', PlayListView.get_context_data, name='Playlist'),
]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from music import views



Urlpatterns = [
	path('', views.music_list),
	path('<int:pk>', views.song_detail)
]
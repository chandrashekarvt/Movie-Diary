from django.urls import path, include
from .views import showMovies, addMovie, editMovie, deleteMovie, searchMovie

urlpatterns = [
    path('', showMovies, name='showMovies'),
    path('add/', addMovie, name='addMovie'),
    path('edit/<int:movie_id>', editMovie, name='editMovie'),
    path('delete/<int:movie_id>', deleteMovie, name='deleteMovie'),
    path('search/', searchMovie, name='searchMovie'),
]
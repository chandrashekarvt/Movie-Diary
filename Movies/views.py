from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Movie
from .infoRetriever import getImageUrl, getTitle, getRatings


def showMovies(request):
    log_user = request.user
    movies = Movie.objects.filter(user=log_user)
    return render(request, 'show-movies.html', {'Movie': movies, 'user': log_user})


def addMovie(request):
    if request.method == 'POST':
        movie_name = request.POST['movie-name']
        mov = movie_name.lower()
        movie_name = mov.replace(' ', '-')
        ratings = getRatings(movie_name)
        title = getTitle(movie_name)
        image_url = getImageUrl(movie_name)

        if title is None:
            title = movie_name
        if image_url is None:
            image_url = 'https://cdn.browshot.com/static/images/not-found.png'

        if ratings is None:
            ratings = 'N/A'
        newMovie = Movie(movie_name=title, image_url=image_url, ratings=ratings, user=request.user)
        newMovie.save()
        return redirect(showMovies)
    else:
        return render(request, 'add-movie.html')


def editMovie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == 'POST':
        movie_name = request.POST['movie-name']
        image_url = request.POST['image-url']
        ratings = request.POST['ratings']
        movie.movie_name = movie_name
        movie.image_url = image_url
        movie.ratings = ratings
        movie.save()
        return redirect(showMovies)
    else:
        return render(request, 'edit-movie.html', {'Movie': movie})


def deleteMovie(request, movie_id):
    Movie.objects.get(id=movie_id).delete()
    return redirect(showMovies)


def searchMovie(request):
    if request.method == 'POST':
        search_value = request.POST['Search']
        movies = Movie.objects.filter(user=request.user, movie_name__contains=str(search_value))
        return render(request, 'show-movies.html', {'Movie': movies, 'user': request.user, 'error': 'No results matching your search :('})

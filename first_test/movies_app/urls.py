from django.urls import path
from . import views
from movies_app.views import MoviesListView, MovieDetailView, \
    Top10MoviesListView, TopRandomMoviesListView, voting


urlpatterns = [
    path('movies', MoviesListView.as_view(), name='movies-list'),
    path('movies/top', Top10MoviesListView.as_view(), name='movies-list'),
    path('movies/top/<int:count>', TopRandomMoviesListView.as_view(),
         name='movies-list'),
    path('movies/<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/<int:pk>/voting', views.voting,
         name='voting')
]

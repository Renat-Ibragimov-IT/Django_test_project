from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from movies_app.models import Movie
from movies_app.forms import MovieForm
from django.shortcuts import render, redirect


class MoviesListView(ListView):
    model = Movie
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(MoviesListView, self).get_context_data(**kwargs)
        context['form'] = MovieForm()
        return context

    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = \
                Movie.objects.create(
                    name=request.POST['name'],
                    description=request.POST['description'],
                    release_date=request.POST['release_date'],
                    rating=request.POST['rating'],
                    duration=request.POST['duration'])
            movie.save()
            return redirect('/movies')
        return HttpResponse('Please enter correct data')


class Top10MoviesListView(ListView):
    model = Movie
    queryset = Movie.objects.order_by('-rating')[:10]
    template_name = "movies_app/top_10_movies.html"


class TopRandomMoviesListView(ListView):
    model = Movie
    paginate_by = 10
    template_name = "movies_app/top_random_movies.html"

    def get_queryset(self):
        count = self.kwargs['count']
        return Movie.objects.order_by('-rating')[:count]


class MovieDetailView(DetailView):
    model = Movie


def voting(request, pk):
    movie = Movie.objects.get(id=pk)
    count = int(request.GET.get('count'))
    movie.vote += count
    movie.save()
    return redirect(f'/movies/{pk}')








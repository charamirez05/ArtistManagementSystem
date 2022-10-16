from django.shortcuts import render
from django.views import View
from .forms import FilmForm
from .models import Actor

# Create your views here.

class FilmView(View):
    template = 'addFilms.html'

    def get(self, request):
        formFilm = FilmForm()
        return render(request, self.template, {'formFilm': formFilm})

    def post(self, request):
        formFilm = FilmForm(request.POST)
        filmActor = Actor.objects.get(pk=request.session['username'])
        if formFilm.is_valid():
            film = formFilm.save()
            film.actor.add(filmActor)

        return render(request, self.template, {'formFilm': formFilm})


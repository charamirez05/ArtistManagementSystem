from django.shortcuts import render
from django.views import View
from .forms import FilmForm
from registration.models import Actor

# Create your views here.

class FilmView(View):
    template = 'addFilms.html'

    def get(self, request):
        formFilm = FilmForm()
        filmActor = Actor.objects.get()
        print(filmActor)
        return render(request, self.template, {'formFilm': formFilm})

    def post(self, request):
        formFilm = FilmForm(request.POST)
        if formFilm.is_valid():
            film = formFilm.save()
            actor = Actor.objects.get(pk=request.session['username'])
            film.actor.add(actor)
            # return redirect(reverse('registration:index'))
        return render(request, self.template, {'formFilm': formFilm})


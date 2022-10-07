from django.shortcuts import render
from django.views import View
from .forms import FilmForm

# Create your views here.

class FilmView(View):
    template = 'addFilms.html'

    def get(self, request):
        formFilm = FilmForm()
        return render(request, self.template, {'formFilm': formFilm})

    def post(self, request):
        formFilm = FilmForm(request.POST)
        if formFilm.is_valid():
            formFilm.save()
            # return redirect(reverse('registration:index'))
        return render(request, self.template, {'formFilm': formFilm})


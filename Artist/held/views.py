from django.shortcuts import render
from django.views import View
from .forms import ConcertForm
from .models import Singer

# Create your views here.

class FilmView(View):
    template = 'addFilms.html'

    def get(self, request):
        formConcert = ConcertForm()
        return render(request, self.template, {'formConcert': formConcert})

    def post(self, request):
        formConcert = ConcertForm(request.POST)
        concertSinger = Singer.objects.get(pk=request.session['username'])
        if formConcert.is_valid():
            concert = formConcert.save()
            concert.singer.add(concertSinger.username)

        return render(request, self.template, {'formConcert': formConcert})


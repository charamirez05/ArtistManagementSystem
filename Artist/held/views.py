from django.db import connection
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import ConcertForm
from registration.models import Singer


# Create your views here.
class ConcertView(View):
    template = 'concert.html'
    def get(self, request):
        formConcert = ConcertForm()
        return render(request, self.template, {'formConcert': formConcert})

    def post(self, request):
        formConcert = ConcertForm(request.POST)
        concertSinger = Singer.objects.get(pk=request.session['username'])
        if formConcert.is_valid():
            concert = formConcert.save()
            singer = concert.singer.add(concertSinger)
            return redirect(reverse('main:dashboard'))

        return render(request, self.template, {'formConcert': formConcert})

class DisplayConcert(View):
    template = 'displayConcert.html'

    def get(self,request):
        cursor = connection.cursor()
        cursor.callproc('dbartist.displayConcert',[request.session['username']])
        concert = cursor.fetchall()
        return render(request, self.template, {'concert':concert})

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import ArtistForm, SingerForm, ActorForm

# Create your views here.

class HomeView(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)


class ArtistView(View):
    template = 'createArtist.html'

    def get(self, request):
        formArtist = ArtistForm()
        return render(request, self.template, {'formArtist': formArtist})

    def post(self, request):
        formArtist = ArtistForm(request.POST)
        isSinger1 = request.POST.get('isSinger', False)
        isActor = request.POST.get('isActor', False)
        if formArtist.is_valid():
            formArtist.save()
            #if isActor == 'on':
            return redirect(reverse('registration:createActor'))
        return render(request, self.template, {'formArtist': formArtist})


class SingerView(View):
    template = 'createSinger.html'

    def get(self, request):
        form = SingerForm()
        return render(request, self.template, {'form': form})


    def post(self, request):
        form = SingerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('registration:index'))
        return render(request, self.template, {'form': form})


class ActorView(View):
    template = 'createActor.html'

    def get(self, request):
        form = ActorForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('registration:index'))
        return render(request, self.template, {'form': form})


    #kekekek

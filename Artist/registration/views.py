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
       # formArtist = SingerForm()
        return render(request, self.template, {'formArtist': formArtist})

    def post(self, request):
        formArtist = ArtistForm(request.POST)
        isSinger = request.POST.get('isSinger', False)
        isActor = request.POST.get('isActor', False)
        if formArtist.is_valid():
            formArtist.save()
            if isActor == 'on':
                return redirect(reverse('registration:createNewActor'))
            elif isSinger == 'on':
                return redirect(reverse('registration:createNewSinger'))
            #elif isSinger == 'on' and isActor == 'on':
            #    return redirect(reverse('registration:createNewSingerActor'))
        return render(request, self.template, {'formArtist': formArtist})


class SingerView(View):
    template = 'createSinger.html'

    def get(self, request):
        formSinger = SingerForm()
        return render(request, self.template, {'formSinger': formSinger})

    def post(self, request):
        formSinger = SingerForm(request.POST)
        if formSinger.is_valid():
            formSinger.save()
            return redirect(reverse('registration:index'))
        return render(request, self.template, {'formSinger': formSinger})


class ActorView(View):
    template = 'createActor.html'

    def get(self, request):
        formActor = ActorForm()
        return render(request, self.template, {'formActor': formActor})

    def post(self, request):
        formActor = ActorForm(request.POST)
        if formActor.is_valid():
            formActor.save()
            #return redirect(reverse('registration:index'))
        return render(request, self.template, {'formActor': formActor})

'''class SingerActorView(View):
    template = 'createSingerActor.html'

    def get(self, request):
        formActor = SingerActorForm()
        return render(request, self.template, {'formActor': formActor})

    def post(self, request):
        formActor = ActorForm(request.POST)
        if formActor.is_valid():
            formActor.save()
            #return redirect(reverse('registration:index'))
        return render(request, self.template, {'formActor': formActor})'''


    #kekekek

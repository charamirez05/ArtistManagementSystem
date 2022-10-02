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
        form = ArtistForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('registration:index'))
        return render(request, self.template, {'form': form})

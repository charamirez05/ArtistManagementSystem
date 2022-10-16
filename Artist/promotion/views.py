from django.shortcuts import render
from django.views import View
from .forms import PlatformForm
from registration.models import Singer


# Create your views here.


class PlatformView(View):
    template = 'promotes.html'

    def get(self, request):
        form = PlatformForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        formPlaform = PlatformForm(request.POST)
        platformSinger = Singer.object.get(pk=request.session['username'])
        if formPlaform.is_valid():
            platform = formPlaform.save()
            platform.singer.add(platformSinger.username)
        return render(request, self.template, {'formPlaform': formPlaform})


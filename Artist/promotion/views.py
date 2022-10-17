from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import PlatformForm
from registration.models import Singer


# Create your views here.


class PlatformView(View):
    template = 'promotes.html'

    def get(self, request):
        formPlaform = PlatformForm()
        return render(request, self.template, {'formPlaform': formPlaform})

    def post(self, request):
        formPlaform = PlatformForm(request.POST)
        platformSinger = Singer.objects.get(pk=request.session['username'])
        if formPlaform.is_valid():
            platform = formPlaform.save()
            singer = platform.singer.add(platformSinger)
            return redirect(reverse('main:dashboard'))

        return render(request, self.template, {'formPlaform': formPlaform})
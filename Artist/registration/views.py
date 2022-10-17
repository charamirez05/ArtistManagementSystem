from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView

from .forms import SingerForm, ActorForm
from .models import Artist, Actor


# Create your views here.

class HomeView(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)


class SingerRegistrationView(View):
    template = 'createSinger.html'

    def get(self, request):
        formSinger = SingerForm()
        return render(request, self.template, {'formSinger': formSinger})

    def post(self, request):
        formSinger = SingerForm(request.POST)
        if formSinger.is_valid():
            formSinger.save()
            return redirect(reverse('registration:login'))
        return render(request, self.template, {'formSinger': formSinger})


class ActorRegistrationView(View):
    template = 'createActor.html'

    def get(self, request):
        formActor = ActorForm()
        return render(request, self.template, {'formActor': formActor})

    def post(self, request):
        formActor = ActorForm(request.POST)
        if formActor.is_valid():
            formActor.save()
            return redirect(reverse('registration:login'))
        return render(request, self.template, {'formActor': formActor})


class LoginView(View):
    template = 'login.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        uname = request.POST['username']
        pwd = request.POST['password']
        print(uname)

        try:
            user = Artist.objects.get(pk=uname)
            if user.password == pwd:
                request.session['username'] = uname
                request.session['isSinger'] = user.isSinger
                request.session['isActor'] = user.isActor
                if request.session['isSinger']:
                    return redirect(reverse('main:dashboard'))
                elif request.session['isActor']:
                    return redirect(reverse('main:dashboard'))

        except Artist.DoesNotExist:
            user = None

        return render(request, self.template, {'msg': 'Incorrect username/ password.'})



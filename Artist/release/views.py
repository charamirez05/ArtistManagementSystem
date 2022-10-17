from django.db import connection
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import AlbumForm, SinglesForm
from registration.models import Singer

from .models import Album


# Create your views here.


class AlbumView(View):
    template = 'albumRelease.html'

    def get(self, request):
        formAlbum = AlbumForm()
        return render(request, self.template, {'formAlbum': formAlbum})

    def post(self, request):
        formAlbum = AlbumForm(request.POST)
        albumSinger = Singer.objects.get(pk=request.session['username'])
        if formAlbum.is_valid():
            album = formAlbum.save(commit=False)
            album.singer = albumSinger
            formAlbum.save()
            return redirect(reverse('main:dashboard'))

        return render(request, self.template, {'formAlbum': formAlbum})


class SinglesView(View):
    template = 'singleRelease.html'

    def get(self, request):
        formSingles = SinglesForm()
        return render(request, self.template, {'formSingles': formSingles})

    def post(self, request):
        formSingles = SinglesForm(request.POST)
        singleSinger = Singer.objects.get(pk=request.session['username'])
        singleAlbum = Album.objects.get(pk=request.POST['album'])
        if formSingles.is_valid():
            single = formSingles.save(commit=False) #fk
            single.singer = singleSinger #fk
            formSingles.save()
            album = single.albums.add(singleAlbum)
            return redirect(reverse('main:dashboard'))
        return render(request, self.template, {'formSingles': formSingles})


class DisplayAlbumView(View):
    template = 'displayAlbum.html'

    def get(self,request):
        cursor = connection.cursor()
        cursor.callproc('dbartist.displayAlbum',[request.session['username']])
        album = cursor.fetchall()
        return render(request, self.template, {'album':album})


class DisplaySingleView(View):
    template = 'displaySingle.html'

    def get(self,request):
        cursor = connection.cursor()
        cursor.callproc('dbartist.displaySingle',[request.session['username']])
        single = cursor.fetchall()
        return render(request, self.template, {'single':single})





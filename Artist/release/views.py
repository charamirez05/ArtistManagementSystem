from django.shortcuts import render
from django.views import View
from .forms import AlbumForm, SinglesForm

# Create your views here.


class AlbumView(View):
    template = 'released.html'

    def get(self, request):
        form = AlbumForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect(reverse('registration:index'))
        return render(request, self.template, {'form': form})


class SinglesView(View):
    template = 'released.html'

    def get(self, request):
        form = SinglesForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = SinglesForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect(reverse('registration:index'))
        return render(request, self.template, {'form': form})

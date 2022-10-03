from django.shortcuts import render
from django.views import View
from .forms import AlbumForm, SingerForm, SinglesForm

# Create your views here.


class ReleaseView(View):
    template = 'released.html'

    def get(self, request):
        form = ReleaseForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = ReleaseForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect(reverse('registration:index'))
        return render(request, self.template, {'form': form})

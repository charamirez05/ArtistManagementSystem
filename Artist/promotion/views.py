from django.shortcuts import render
from django.views import View
from .forms import PlatformForm

# Create your views here.


class PlatformView(View):
    template = 'promotes.html'

    def get(self, request):
        form = PlatformForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = PlatformForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect(reverse('registration:index'))
        return render(request, self.template, {'form': form})

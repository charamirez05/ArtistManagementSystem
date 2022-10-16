from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

# Create your views here.

class HomeView(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)



class DashboardView(View):
    template = 'dashboard.html'

    def get(self, request):
        return render(request, self.template)
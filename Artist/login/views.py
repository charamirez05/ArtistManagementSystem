from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


# Create your views here.


class LoginView(View):
    template = 'login.html'

    def get(self, request):
        return render(request, self.template)

    '''def post(self, request):
        uname = request.POST['username']
        pwd = request.POST['password']

        try:
            user = Artist.objects.get(pk=uname)
            if user.password == pwd:
                request.session['username'] = user.username
                request.session['type'] = user.type
                return redirect(reverse('registration:index'))
        except Artist.DoesNotExist:
            user = None

        return render(request, self.template,{'msg':'Incorrect username/ password.'})'''
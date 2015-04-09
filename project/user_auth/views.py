from django.shortcuts import render
from django.http import HttpResponse

from .models import Person
from .forms import SignUpForm


def worker_signup(request):
    if request.method == 'GET':
        # return the login form
        form = SignUpForm()
        return render(request, 'user_auth/w_login.html', context={'form': form})

    elif request.method == 'POST' and request.POST:
        # submit the form
        form = SignUpForm(request.POST)

        if form.is_valid():

            person = Person(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                country=form.cleaned_data['country'],
                phone=form.cleaned_data['phone'],
                about=form.cleaned_data['about'],
                who='w'
            )
            person.save()

            return HttpResponse("Valid Form Submission")
        else:
            return render(request, 'w_login.html', context={'form': form})

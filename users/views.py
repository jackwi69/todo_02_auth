from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm

def register(request):
    # form = UserCreationForm()
    form = UserRegisterForm()
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data('username')
            # messages.success(request, f'{username}, your account was created successfully')
        # else:
        #     form = UserCreationForm()
    context = {'form':form}
    return render(request, 'users/register.html', context)

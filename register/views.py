from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm
from .models import User, UserManager

def register(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
           
            # Save the User object
            new_user.save()
            return render(request, 'lk.html', {'user': new_user})
    else:
        user_form = SignUpForm()
    return render(request, 'register.html', {'user_form': user_form})
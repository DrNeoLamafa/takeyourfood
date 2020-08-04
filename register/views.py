from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm, LkForm
from .models import User, UserManager, Client, Courier, Rest

def register(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
           
            # Save the User object
            new_user.save()
            if request.POST.get("role") == 'client':
                new_client = Client()
                new_client.user = new_user
                new_client.email = request.POST.get("email")
                new_client.save()

            if request.POST.get("role") == 'Cour':
                new_client = Courier()
                new_client.user = new_user
                new_client.email = request.POST.get("email")
                new_client.save()

            if request.POST.get("role") == 'REST':
                new_client = Rest()
                new_client.user = new_user
                new_client.email = request.POST.get("email")
                new_client.save()
            return render(request, 'lk.html', {'user': new_user})
    else:
        user_form = SignUpForm()
    return render(request, 'register.html', {'user_form': user_form})
    
def LkRender(request):
   
    user_form = LkForm()
    return render(request, 'lk.html', {'lkform': user_form})

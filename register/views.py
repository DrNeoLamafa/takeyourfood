from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm, LkForm, LkFormClient, LkFormCourier, LkFormFood
from .models import User, UserManager, Client, Courier, Rest, Food
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            new_user.save()
            if request.POST.get("role") == 'client':
                new_client = Client()
                new_client.user = new_user
                new_client.email = request.POST.get("email")
                new_client.save()
                new_user.client = new_client
                new_user.save()

            if request.POST.get("role") == 'Cour':
                new_client = Courier()
                new_client.user = new_user
                new_client.email = request.POST.get("email")
                new_client.save()
                new_user.courier = new_client
                new_user.save()

            if request.POST.get("role") == 'REST':
                new_client = Rest()
                new_client.user = new_user
                new_client.email = request.POST.get("email")
                new_client.save()
                new_user.rest = new_client
                new_user.save()
            return redirect('login')
    else:
        user_form = SignUpForm()
    return render(request, 'register.html', {'user_form': user_form})
    

@login_required
def LkRender(request):
    user = User.objects.get(pk=request.user.pk)

    if request.method == 'POST':
        courier_form = LkFormCourier()
        client_form = LkFormClient()
        rest_form = LkForm()
        if 'dataform' in request.POST:
            courier_form = LkFormCourier()
            client_form = LkFormClient()
            rest_form = LkForm()
            
            if (user.role =='Cour'):
                courier_form = LkFormCourier(request.POST)
            if (user.role =='client'):
                client_form = LkFormClient(request.POST)
            if (user.role =='REST'):   
                rest_form = LkForm(request.POST, request.FILES)
                food_form = LkFormFood()
            if courier_form.is_valid():
            
                courier = user.courier
                courier.name = request.POST.get("name")
                courier.famil = request.POST.get("famil")
                courier.status = 1
                courier.save()
            if client_form.is_valid():
            
                client = user.client
                client.name = request.POST.get("name")
                client.famil = request.POST.get("famil")
                client.mobil = request.POST.get("mobil")
                client.save()
            if rest_form.is_valid():
              
                rest = user.rest
                rest.name_res = request.POST.get("name_res")
                rest.addres = request.POST.get("addres")
                rest.category = request.POST.get("category")
                rest.discription = request.POST.get("discription")
                rest.image = rest_form.cleaned_data['image']
                rest.save()
           
        elif 'foodform' in request.POST:
            food_form = LkFormFood(request.POST, request.FILES)
            courier_form = LkFormCourier()
            client_form = LkFormClient()
            rest_form = LkForm()
          
            if food_form.is_valid():
                food = Food()
                food.name = request.POST.get("name")
                food.category = request.POST.get("category")
                food.price = request.POST.get("price")
                food.image = food_form.cleaned_data['image']
                user.rest.food_set.add(food, bulk =False)
                user.rest.save()
                food.save()
            
    else:
        courier_form = LkFormCourier()
        client_form = LkFormClient()
        rest_form = LkForm()
        food_form = LkFormFood()
     
    return render(request, 'lk.html', {'lkform': rest_form, 'lkformcourier': courier_form, 'lkformclient': client_form, 'foodform': food_form })




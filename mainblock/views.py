from django.shortcuts import render
from django.http import HttpResponse
from register.models import Rest, Food

def index(request):
    
    restlist = Rest.objects.all()
    
    all_rest = []
    for rest in restlist:
        
        
        rest_info = {
                
            'rest_name': rest.name_res,
            'img': rest.image,
            'discription': rest.discription,
            'category': rest.category,
            'slug': rest.slug,
        

        }
        all_rest.append(rest_info)

    return render(request, "index.html", {'list': all_rest})
def foodlist(request, slug):
    rest = Rest.objects.get(slug__iexact=slug)
    
    print(1)
    foodlist = Food.objects.filter(rest=rest)
    args = {'slug_arg': slug}
    all_food = []
    for food in foodlist:
        
        
        food_info = {
                
            'name': food.name,
            'price': food.price,
            'category': food.category,
            'image': food.image
        

        }
        all_food.append(food_info)

    return render(request, "foodlist.html", args, {'list': all_food})

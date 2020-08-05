from django.shortcuts import render
from django.http import HttpResponse
from register.models import Rest

def index(request):
    restlist = Rest.objects.all()
    
    all_rest = []
    for rest in restlist:
        
        
        rest_info = {
          
            'rest_name': rest.name_res,
            'img': rest.image
        

        }
        all_rest.append(rest_info)

    return render(request, "index.html", {'list': all_rest})


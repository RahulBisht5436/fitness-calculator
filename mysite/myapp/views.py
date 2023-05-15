from django.shortcuts import render,redirect
from .models import Food,consumed

# Create your views here.
def index(request):
    if request.method=="POST":
        food=request.POST['food_consumed']
        food=Food.objects.get(name=food)
        user=request.user
        consumed.objects.create(user=user,food_consumed=food)
    
    fooding=consumed.objects.filter(user=request.user)

    foods=Food.objects.all()
    return render(request,'foodapp/index.html',{'foods':foods,'fooding':fooding})

def del_consume(request,id):
    consumed_food=consumed.objects.get(id=id)
    
    consumed.delete()
        
    return render

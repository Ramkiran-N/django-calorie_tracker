from django.shortcuts import render,redirect
from .models import Food,Consume
# Create your views here.
def index(request):
    if request.method =='POST':
        food_consumed = request.POST.get('food_consumed')
        food_obj = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user = user,food_consumed = food_obj)
        consume.save()
    data = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    return render(request,'food/index.html',{'data':data,'consumed_food':consumed_food})

def delete_data(request,id):
    data = Consume.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('index')
    return render(request,'food/delete-form.html',{'data':data})
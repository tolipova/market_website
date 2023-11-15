from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q
# Create your views here.
def items(request):
    if 'q' in request.GET:
        qidirish = request.GET['q']
        umumiy = Q(item_name__icontains=qidirish.lower())
        post = Item.objects.filter(umumiy)
    else:
        post = Item.objects.all()    
    context = {'post':post}
    return render(request, 'index.html', context)

def add(request):
    form = MarketForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('items')
    else:
        form = MarketForm()    
    return render(request, 'add.html', {'form':form})   


def delete(request, id):
    post = Item.objects.get(id=id)
    post.delete()
    return redirect('items')



def edit(request,id):
    post = Item.objects.get(id=id)
    context = {
        'post':post
    }
    return render(request, 'update.html', context)

def editrecord(request,id):
    category = request.POST['category']
    item_name = request.POST['item_name']
    price = request.POST['price']
    quantity = request.POST['price']
    expiration_date  = request.POST['price']
    paymet = request.POST['price']

    info = Item.objects.get(id=id)
    info.category = category
    info.item_name = item_name
    info.price = price
    info.quantity = quantity
    info.expiration_date = expiration_date
    info.paymet = paymet


    info.save()
    return redirect('items')
    

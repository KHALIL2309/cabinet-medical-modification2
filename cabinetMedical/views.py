from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.

from .models import *

from .forms import OrderForm

from .filters import OrderFilter





def client(request,pk):
    client = Client.objects.get(id=pk)
    orders = client.order_set.all()
    num_order = orders.count()

    searchFilter = OrderFilter(request.GET , queryset=orders)
    orders = searchFilter.qs

    context={
        'client' : client , 
        'orders' : orders ,
        'num_order' : num_order,
        'searchFilter' : searchFilter}
        
    return render (request , 'cabinetMedical/client.html', context)

def about(request):
    return HttpResponse('heee about')
      

def home(request):
    vclient = Client.objects.all()
    t_age = vclient.filter(age='20').count()
    vorder = Order.objects.all()
    t_orders = vorder.count()
    a_orders = vorder.filter(status='arrived').count()
    l_orders = vorder.filter(status='lost').count()
    d_orders = vorder.filter(status='did_not_arrive').count()
    context = {'vclients' : vclient,
                't_age' : t_age ,
                'order': vorder ,
                't_orders' : t_orders,
                'a_orders' : a_orders,
                'l_orders' : l_orders,
                'd_orders' : d_orders, 
                }

    return render (request , 'cabinetMedical/home.html',context)   

def boook(request):
    vbook = book.objects.all()
    return render (request , 'cabinetMedical/book.html',{'Book': vbook})   

def create(request):
    form = OrderForm()
    if request.method == 'POST':    # pour sécurité
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # pour rediriger les informations sur la page
    context = {'form' : form}
                
    return render (request , 'cabinetMedical/My_order_form.html',context)


def update(request , pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST , instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form' : form}
                
    return render (request , 'cabinetMedical/My_order_form.html',context)



def delete(request , pk):
    order = Order.objects.get(id=pk)
    context = {'order' : order}
    if request.method == 'POST':
        order.delete()
        return redirect('/')
                
    return render (request , 'cabinetMedical/delete_form.html',context)

# http://127.0.0.1:8000/
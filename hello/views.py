from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product


def home(request):
    hello=Product.objects
    return render(request,'home.html',{'hello':hello})

def help(request):
    return render(request,'help.html')   

def warriors(request):
    return render(request,'warriors.html')

   
@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['Name'] and request.POST['Full_Address']  and request.FILES['image'] and request.FILES['self_image']:
            product = Product()
            product.Name = request.POST['Name']
            product.Full_Address = request.POST['Full_Address']
            product.image = request.FILES['image']
            product.self_image = request.FILES['self_image']
            product.hunter = request.user
            product.save()
            return redirect('/hello/'+str (product.id))
        else:
            return render(request, 'create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'create.html') 


def detail(request,product_id):
    product= get_object_or_404(Product,pk=product_id)
    return render(request, 'detail.html',{'product':product})             


@login_required(login_url="/account/signup")
def upvote(request,product_id):
    if request.method=='POST':
        product= get_object_or_404(Product,pk=product_id)
        product.votes_total+=1
        product.save()
        return redirect('/hello/'+str(product.id))    
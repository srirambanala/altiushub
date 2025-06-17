from django.shortcuts import render,redirect,get_object_or_404,reverse
from .models import Product

# Create your views here.

#display all products in home page
def HomePage(request):                                            
    context=Product.objects.all()
    return render(request,'products/list.html',{'context':context})

# to update a product
# def update(request,id):
#     form= request.POST 
#     if form.is_valid():
#         product = Product.objects.get(id=id)

#         if request.method == 'POST':
#             id = request.POST.get('id')
#             location = request.POST.get('location')
#             rent = request.POST.get('rent')
#             bed_rooms = request.POST.get('bed_rooms')

#             product.Location = location
#             product.Rent = rent
#             product.Bed_rooms = bed_rooms
#             product.save()
#             return render(request, 'products/update.html', {'product': product})
    
#     else:
#         return render(request,'products/update.html',{'product':None})
    
# #delete a product
# def delete(request,id):
#     if request.method=='POST':
#         id=request.POST.get('id')
#         product=get_object_or_404(Product, pk=id)
#         product.delete()
#         return redirect('products:home')
#     else:
#         product = get_object_or_404(Product, pk=id)
#         return render(request, 'products/delete.html', {'product': product})
    

def delete_product(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return redirect('products:home')
    else:
        product = get_object_or_404(Product, pk=id)
        return render(request, 'products/delete.html', {'product': product})

#search box implementation
def search_results(request,query):
    if request.method == 'POST':
        query = request.POST.get('query')
        min_amount= request.POST.get('min_amount')
        max_amount = request.POST.get('max_amount')
        results = Product.objects.filter(location__icontains=query)
        if min_amount and max_amount:
            results = results.filter(rent__gte=min_amount, rent__lte=max_amount)
        elif min_amount:
            results = results.filter(rent__gte=min_amount)
        elif max_amount:
            results = results.filter(rent__lte=max_amount)

        return render(request, 'products/search_results.html', {'results': results, 'query': query})
    else:
        return render(request, 'products/search_results.html', {'results': [], 'query': ''})
    

def update_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product.location = request.POST.get('location')
        product.rent = request.POST.get('rent')
        product.bed_rooms = request.POST.get('bed_rooms')
        product.save()
        return redirect('products:home')
    return render(request, 'products/update.html', {'product': product})

# def search_results(request, query):
#     if request.method == 'POST':
#         query = request.POST.get('query')
#         results = Product.objects.filter(location__icontains=query)
#         return render(request, 'search_results.html', {'results': results, 'query': query})
#     else:
#         return redirect('products:home')
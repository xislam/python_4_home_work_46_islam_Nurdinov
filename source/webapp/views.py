
from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import ProductForm
from webapp.models import Product


def index_view(request, *args, **kwargs):
    product = Product.objects.all()
    return render(request, 'index.html', context={
        'products': products
    })


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product})


def product_create_view(request, *args, **kwargs):
    if request.method == 'GET':

        form = ProductForm()

        return render(request, 'create.html', context={'form': form})

    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name_of_product=form.cleaned_data['name_of_product'],
                date=form.cleaned_data['date'],
                description=form.cleaned_data['description'],
                count=form.cleaned_data['count'],
                status=form.cleaned_data['status']

            )

            return redirect('product_view', pk=product.pk)

        else:

            return render(request, 'create.html', context={'form': form})


def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(data=request.POST)

    if request.method == 'GET':
        form = ProductForm(data={
            'name_of_product': product.name_of_product,
            'description': product.description,
            'status': product.status,
            'date': product.date,
            'count': product.count

        })
        return render(request, 'update.html', context={'product': product, 'form': form})

    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name_of_product = form.cleaned_data['name_of_product']
            product.date = form.cleaned_data['date']
            product.status = form.cleaned_data['status']
            product.description = form.cleaned_data['description']
            product.count = form.cleaned_data['count']
            product.save()
            return redirect('product_view', pk=product.pk)


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        return render(request, 'delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('index')

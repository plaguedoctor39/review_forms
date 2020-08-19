from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()
    print(products)

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)

    if request.method == 'POST':
        # логика для добавления отзыва
        form = ReviewForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = ReviewForm()
    reviews = list(Review.objects.filter(product=product))
    context = {
        'form': form,
        'product': product,
        'reviews': reviews
    }

    return render(request, template, context)

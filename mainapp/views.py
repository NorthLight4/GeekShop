from django.shortcuts import render
from .models import ProductCategory, Product


def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)



def products(request, pk=None):
    title = 'продукты'
    same_products = Product.objects.all()[:4]
    links_menu = ProductCategory.objects.all()
    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', content)

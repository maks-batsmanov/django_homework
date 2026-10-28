from django.shortcuts import get_object_or_404

from catalog.models import Category, Product


def  get_products_by_category(category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    return products
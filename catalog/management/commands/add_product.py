from django.core.management.base import BaseCommand

from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category = Category.objects.create(name='Гитары', description='Шестиструнные гитары на любой вкус')

        products = [
            {'name': 'fender', 'description': 'Лучший звук', 'category': category, 'price': 15000},
            {'name': 'yamaha', 'description': 'Приятные обертона', 'category': category, 'price': 16000},
            {'name': 'gibson', 'description': 'Баланс качеств', 'category': category, 'price': 17000}
        ]

        for products_data in products:
            product, created = Product.objects.get_or_create(**products_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))

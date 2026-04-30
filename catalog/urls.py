from django.urls import path
from .views import ProductDetailView, ProductCreateView, ProductListView, ContactsView

app_name = 'catalog'

urlpatterns = [

    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('', ProductListView.as_view(), name='home'),
    path('home/', ProductListView.as_view(), name='home'),
    path("contacts/", ContactsView.as_view(), name='contacts'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/create/', ProductCreateView.as_view(), name='form_add_product')
]

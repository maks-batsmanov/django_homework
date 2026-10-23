from django.urls import path
from .views import (
    ProductDetailView,
    ProductCreateView,
    ProductListView,
    ContactsView,
    ProductDeleteView,
    ProductPublicationStatusToggle,
    ProductUpdateView, ListCategories, ProductsByCategory
)

app_name = 'catalog'

urlpatterns = [

    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('', ProductListView.as_view(), name='home'),
    path('home/', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/toggle-publication/', ProductPublicationStatusToggle.as_view(), name='product_publication_toggle'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('categories/', ListCategories.as_view(), name='category_list'),
    path('category/<int:pk>/products/', ProductsByCategory.as_view(), name='category_products'),

]

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from .models import Product
from .forms import AddProductForm, ContactForm


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    paginate_by = 6


class ContactsView(LoginRequiredMixin, FormView):
    model = Product
    template_name = 'catalog/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']

        return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено.')


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/detail.html'
    context_object_name = 'product'

def product_create_view(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = AddProductForm()
    return render(request, 'catalog/form_add_product.html', {'form': form})


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'catalog/form_add_product.html'
    form_class = AddProductForm
    success_url = reverse_lazy('catalog:form_add_product')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/delete_product.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.delete_product'


class ProductPublicationStatusToggle(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.publication_status = not product.publication_status
        product.save()
        return redirect('catalog:product_detail', pk=pk)

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView, DeleteView, View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

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
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/delete_product.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:home')

    def test_func(self):
        product = self.get_object()
        is_owner = product.owner == self.request.user
        is_moderator = self.request.user.groups.filter(name='Product moderator').exists()
        return is_owner or is_moderator

class ProductPublicationStatusToggle(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.publication_status = not product.publication_status
        product.save()
        return redirect('catalog:product_detail', pk=pk)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'catalog/form_add_product.html'
    form_class = AddProductForm

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={"pk": self.object.pk})

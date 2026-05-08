from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import AddEntryForm
from blog.models import BlogEntry


class BlogCreateView(CreateView):
    model = BlogEntry
    template_name = 'blog/blogentry_create.html'
    form_class = AddEntryForm
    success_url = reverse_lazy('blog:list')


class BlogUpdateView(UpdateView):
    model = BlogEntry
    template_name = 'blog/blogentry_create.html'
    form_class = AddEntryForm

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'pk': self.object.pk})


class BlogListView(ListView):
    model = BlogEntry

    def get_queryset(self):
        queryset = BlogEntry.objects.all()
        if not self.request.user.is_staff:
            queryset = queryset.filter(publication_attribute=True)
        return queryset


class BlogDetailView(DetailView):
    model = BlogEntry
    template_name = 'blog/blogentry_detail.html'
    context_object_name = 'entry'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save(update_fields=['views'])
        return obj


class BlogDeleteView(DeleteView):
    model = BlogEntry
    template_name = 'blog/blogentry_confirm_delete.html'
    context_object_name = 'entry'
    success_url = reverse_lazy('blog:list')

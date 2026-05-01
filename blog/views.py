from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView

from blog.forms import AddEntryForm
from blog.models import BlogEntry


class BlogListView(ListView):
    model = BlogEntry

    def get_queryset(self):
        queryset = BlogEntry.objects.all()
        if not self.request.user.is_staff:
            queryset = queryset.filter(publication_attribute=True)
        return queryset


class BlogCreateView(CreateView):
    model = BlogEntry
    template_name = 'blog/blogentry_create.html'
    form_class = AddEntryForm
    success_url = reverse_lazy('blog:list')

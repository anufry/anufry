from django.views.generic import View, ListView, DetailView
from django.db.models import Q
# from django.shortcuts import get_object_or_404

from .models import Post

class PostList(ListView):
    model = Post
    context_object_name = 'list'
    template_name = 'blog/list.html'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.all()
        
        if self.get_search_term():
            qs = qs.filter(Q(title__icontains=self.get_search_term()) | Q(teaser__icontains=self.get_search_term()))

        # print('--qs =', qs.query)

        return qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.get_search_term()
        return context


    def get_search_term(self):
        search = self.request.GET.get('search', None)
        if search:
            return search.strip()
        return None

 

class PostItem(DetailView):
    model = Post
    template_name = 'blog/item.html'
    context_object_name = 'item'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['simmilar_items'] = self.get_simmilar_items(context['item'])
        # print('-- context =', context)
        return context


    def get_simmilar_items(self, item):
        return Post.objects.exclude(id=item.id)[:4]
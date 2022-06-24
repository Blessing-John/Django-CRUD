from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostCreate(generic.CreateView):
    model = Post
    fields = __all__
    success_url  = reverse_lazy(“blog:all”)
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostUpdate(generic.UpdateView):
    model = Post
    fields = __all__
    success_url  = reverse_lazy(“blog:all”)
    template_name = 'index.html'  

class PostDelete(generic.DeleteView):
    model = Post
    fields = __all__
    success_url  = reverse_lazy(“blog:all”)
    template_name = 'index.html'  
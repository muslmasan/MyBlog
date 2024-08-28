from .models import Post
from . forms import PostForm,UpdateForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,DetailView ,TemplateView
# Create your views here.
# the post views 
class Post_list (ListView):
    model=Post
    context_object_name='posts'
    template_name='blog/home/index.html'
    
class Post_detail(DetailView):
    model= Post
    context_object_name='post'
    template_name='blog/home/post.html'

class Create_Post(CreateView):
    model=Post
    form_class=PostForm
    template_name='blog/home/create.html'
    success_url='/'

class Delete_Post(DeleteView):
    model=Post
    template_name='blog/home/delete.html'
    success_url='/'

class Update_post(UpdateView):
    model=Post
    template_name='blog/home/create.html'
    form_class= UpdateForm
    success_url= reverse_lazy('post_list')

class Author_view(TemplateView):
    template_name = 'blog/home/author.html'
# the user 
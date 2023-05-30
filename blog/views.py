from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy
# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = "home.html"
    context_object_name = 'blogs'
    

class BlogDetail(DetailView):
    model = Blog
    template_name='blog.html'
    context_object_name = 'blog'
    
class BlogCreateView(CreateView):
    model = Blog
    template_name = "create_blog.html"
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "update_blog.html"
    fields = ['title', 'body']
    
class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "delete_blog.html"
    success_url = reverse_lazy('home') #so that it won't execute the url until the view has finished

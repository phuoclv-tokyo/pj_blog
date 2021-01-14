from django.views.generic import ListView, DetailView
from .models import Post

class Index(ListView):
    model = Post

class Detail(DetailView):
    model = Post
    
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class Create(CreateView):
    model = Post
    
    fields = ["title", "body", "category", "tags"]

class Update(UpdateView):
    model = Post
    
    fields = ["title", "body", "category", "tags"]

class Delete(DeleteView):
    model = Post
    
    success_url = "/"
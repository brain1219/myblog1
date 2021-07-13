from django.shortcuts import render
from blog.models import Category, Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

# Create your views here.
def index(req):
    post_latest = Post.objects.order_by("-createDate") # - : 내림차순, [:5] : 5개를 가져옴 
    allCategories = Category.objects.order_by("name")
    context = {
        "post_latest": post_latest,
        "allCategories": allCategories,
    }

    return render(req, "index.html", context=context)

class PostDetailView(generic.DetailView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "title_image", "content", "category"]

from django.shortcuts import render
from blog.forms import CommentForm
from .models import Post, Comment, Category


def home(request):
 return render(request, 'Site/index.html')

def testimonials(request):
 return render(request, 'Site/testimonials.html')

def about(request):
 return render(request, 'Site/about.html')

def contact(request):
 return render(request, 'Site/contact.html')

def tutorials(request):
    return render(request, 'Site/tutorials.html')

def tutorial_single(request):
    return render(request, 'tutorial-single.html')

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {"posts": posts}
    return render(request, "Site/blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "posts": posts}
    return render(request, "Site/blog_category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "Site/blog_detail.html", context)

def react(request,category):
    posts = Post.objects.all(categories__name__contains=category).filter(name = "React")
    context = {"posts": posts}
    return render(request, "Site/react.html", context)
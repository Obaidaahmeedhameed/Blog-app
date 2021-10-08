from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import  login_required, user_passes_test

from .models import Post
from .forms import CreatePostForm


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})


# def user_check(user, **kwargs):
#     print('post, ', user)
#     print(kwargs)
#     return 

@login_required
def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            form.save()
            messages.success(request, "Post Successfully created!")
            return redirect('blog:detail_post', slug=obj.slug)
    else:
        form = CreatePostForm()

    return render(request, 'create_post.html', {'form':form})

@login_required
def update_post(request, slug):
    
    post = get_object_or_404(Post, slug=slug)
    form = CreatePostForm(request.POST or None, instance = post)
    if form.is_valid():
        form.save()
        messages.success(request, "Post Successfully updated!")
        return HttpResponseRedirect('/')

    return render(request, 'create_post.html', {'form':form})

def detail_post(request, slug):
    
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'detail_post.html', {'post':post})

@login_required
def delete_confirm(request,slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request,'deletconfg.html',{'post':post})
    
@login_required
def delete_post(request,slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return HttpResponseRedirect('/')
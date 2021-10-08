from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from  django.contrib.auth.models import  User
from django.contrib.auth.decorators import  login_required

from blog.models import Post
from .forms import UserCreateForm


def register(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Successfully created!")
            return redirect('users:login')
    else:
        form = UserCreateForm()

    return render(request, 'users/create_user.html', {'form':form})


@login_required()
def profile(request, pk):

    user = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(author=user)
    return render(request, 'users/profile.html', {'posts':posts, 'object':user})

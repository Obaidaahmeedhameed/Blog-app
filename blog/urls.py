from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('create/post/', views.create_post, name='create_post'),
    path('post/edit/<slug:slug>/', views.update_post , name='update_post'),
    path('post/<slug:slug>/', views.detail_post , name='detail_post'),
    path('delete/confirm/<slug:slug>/', views.delete_confirm,name='delete_post'),
    path('delete/<slug:slug>/', views.delete_post,name='delete'),
    
]
from django.urls import path, include
from django.contrib import admin
from django.urls.resolvers import URLPattern
from .import views
from django.conf.urls import url

urlpatterns  = [

path('', views.home, name="home"),
path('testimonials/', views.testimonials, name = "testimonials"),
path('about/', views.about, name="about"),
path('contact/', views.contact, name="contact"),
path('tutorials/', views.tutorials, name="blog_index"),
path('tutorial_single/', views.tutorial_single, name="tutorial-single"),
path("blog/", views.blog_index, name="blog_index"),
path("<int:pk>/", views.blog_detail, name="blog_detail"),
path("<category>/", views.blog_category, name="blog_category"),
path('react/', views.react, name="react")
]


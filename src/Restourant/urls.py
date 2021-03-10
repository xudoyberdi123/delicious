from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("recipe/<int:recipe_id>", views.recipe_with_id, name="recipe"),
    path("recipes/", views.recipes, name="recipes"),
    path("elements/", views.elements, name="elements"),
    path("blog-post/", views.blog_post, name="blog_post"),
]

from django.shortcuts import render, get_object_or_404
from .models import *

def index(requests):

    recipies = Recipes.objects.all().order_by("-created_at")

    ctx = {
        "recipes": recipies
    }

    return render(requests, "index.html", ctx)


def recipes(requests):
    # noinspection SpellCheckingInspection
    recipies = Recipes.objects.all()
    ctg = Category.objects.all()
    l1 = []
    if requests.GET:
        var = requests.GET.get("search")
        var_ctg = requests.GET.get("category")
        print(var_ctg,type(var_ctg))
        if int(var_ctg) != 0:
            print("if")
            srch_where = Recipes.objects.all().filter(category_id_id=var_ctg)
        else:
            srch_where = Recipes.objects.all()
        print(srch_where)
        for i in srch_where:
            if str(var).lower() in str(i.title).lower():
                l1.append(i)

    ctx = {
        "recipes": recipies,
        "ctg": ctg,
        "l1": l1
    }
    render(requests, "nav.html", ctx)
    return render(requests, "receipe-post.html", ctx)


def recipe_with_id(requests, recipe_id):
    recipe = get_object_or_404(Recipes, pk=recipe_id)
    # noinspection SpellCheckingInspection
    recipies = Recipes.objects.all()
    ctg = Category.objects.all()


    ctx = {
        "recipe": recipe,
        "recipes": recipies,
        "ctg": ctg,
    }
    render(requests, "nav.html", ctx)
    return render(requests, "receipe_with_id.html", ctx)


def about(requests):
    sgt = Suggestions()
    if requests.POST:
        sgt.name = requests.POST.get("username")
        sgt.email = requests.POST.get("email")
        sgt.subject = requests.POST.get("subject")
        sgt.message = requests.POST.get("message")
        sgt.save()
    return render(requests, "about.html", {})


def blog_post(requests):
    blog = BlogAndPost.objects.all().order_by("-created_at")
    ctx = {
        "blog": blog

    }
    return render(requests, "blog-post.html", ctx)


def contact(requests):
    sgt = Suggestions()
    if requests.POST:
        sgt.name = requests.POST.get("username")
        sgt.email = requests.POST.get("email")
        sgt.subject = requests.POST.get("subject")
        sgt.message = requests.POST.get("message")
        sgt.save()
    return render(requests, "contact.html", {})


def elements(requests):
    return render(requests, "elements.html", {})

from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import *
from .forms import SuggestionsForm


def index(requests):
    new = NewsLetter()
    list_news_email = []
    for i in NewsLetter.objects.all():
        list_news_email.append(i.email)
    if requests.POST.get("news_email"):
        if requests.POST.get("news_email") not in list_news_email:
            new.email = requests.POST.get("news_email")
            new.save()

    recipies = Recipes.objects.all().order_by("-created_at")
    ctgs_for_nav = Category.objects.all()
    small_comment = []
    for i in recipies:
        small_comment.append(len(Suggestions.objects.filter(recipe_id=i.id)))
    ctx = {
        "recipes": recipies,
        "small": zip(recipies, small_comment),
        "star": [1, 2, 3, 4, 5],
        "ctgs_for_nav": ctgs_for_nav
    }
    render(requests, "nav.html", ctx)
    return render(requests, "index.html", ctx)


def recipes(requests):
    ctgs_for_nav = Category.objects.all()
    # noinspection SpellCheckingInspection
    recipies = Recipes.objects.all().order_by("-created_at")
    ctg = Category.objects.all()
    l1 = []
    if requests.GET:
        var = requests.GET.get("search")
        var_ctg = requests.GET.get("category")
        if int(var_ctg) != 0:
            srch_where = Recipes.objects.all().filter(category_id_id=var_ctg)
        else:
            srch_where = Recipes.objects.all()
        for i in srch_where:
            if str(var).lower() in str(i.title).lower():
                l1.append(i)
    else:
        l1 = recipies
    ctx = {
        "recipes": recipies,
        "ctg": ctg,
        "l1": l1,
        "star": [1, 2, 3, 4, 5],
        "ctgs_for_nav": ctgs_for_nav
    }
    render(requests, "nav.html", ctx)
    return render(requests, "receipe-post.html", ctx)


def recipe_with_id(requests, recipe_id):
    ctgs_for_nav = Category.objects.all()
    recipe = get_object_or_404(Recipes, pk=recipe_id)
    # noinspection SpellCheckingInspection
    recipies = Recipes.objects.all()
    ctg = Category.objects.all()
    form = SuggestionsForm(requests.POST or None)
    if requests.POST:
        if form.is_valid():
            form.save()

    ctx = {
        "recipe": recipe,
        "recipes": recipies,
        "ctg": ctg,
        "star": [1, 2, 3, 4, 5],
        "ctgs_for_nav": ctgs_for_nav
    }
    return render(requests, "receipe_with_id.html", ctx)


def about(requests):
    ctgs_for_nav = Category.objects.all()
    all_recipes = get_list_or_404(Recipes)
    all_ctg = get_list_or_404(Category)
    all_recipes_leng = len(all_recipes)
    ctg_counter_all = {}

    for i in all_recipes:
        for j in all_ctg:
            if j.name == i.category_id.name:
                ctg_counter_all[j.name] = [len(Recipes.objects.filter(category_id=j.id)), j]

    sgt = ContactUs()
    if requests.POST:
        sgt.name = requests.POST.get("username")
        sgt.email = requests.POST.get("email")
        sgt.subject = requests.POST.get("subject")
        sgt.message = requests.POST.get("message")
        sgt.save()
    ctx = {
        "all": all_recipes_leng,
        "all_ctg_absolute": zip(all_ctg, ctg_counter_all),
        "all_recipes": all_recipes,
        "all_ctg": ctg_counter_all,
        "ctgs_for_nav": ctgs_for_nav

        }
    return render(requests, "about.html", ctx)


def blog_post(requests):
    ctgs_for_nav = Category.objects.all()
    blog = BlogAndPost.objects.all().order_by("-created_at")
    ctx = {
        "blog": blog,
        "ctgs_for_nav": ctgs_for_nav
    }
    return render(requests, "blog-post.html", ctx)


def contact(requests):
    new = NewsLetter()
    list_news_email = []
    for i in NewsLetter.objects.all():
        list_news_email.append(i.email)
    if requests.POST.get("news_email"):
        if requests.POST.get("news_email") not in list_news_email:
            new.email = requests.POST.get("news_email")
            new.save()

    ctgs_for_nav = Category.objects.all()
    sgt = ContactUs()
    if requests.POST.get("email"):
        sgt.name = requests.POST.get("username")
        sgt.email = requests.POST.get("email")
        sgt.subject = requests.POST.get("subject")
        sgt.message = requests.POST.get("message")
        sgt.save()
    return render(requests, "contact.html", {"ctgs_for_nav": ctgs_for_nav})

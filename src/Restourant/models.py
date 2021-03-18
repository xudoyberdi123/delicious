from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField()

    def __str__(self):
        return self.name


class Reyting(models.Model):
    type = models.CharField(max_length=32, null=False, default=[])

    def __str__(self):
        return self.type


class Recipes(models.Model):
    title = models.CharField(max_length=64)
    prep_time_min = models.IntegerField(null=False)
    cook_time_min = models.IntegerField(null=False)
    yields = models.IntegerField(null=False)
    image = models.ImageField(null=False)
    ingredients = models.JSONField(null=False, blank=True)
    steps = models.JSONField(null=False, blank=True)
    created_at = models.TimeField(auto_now_add=True)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    reyting_id = models.ForeignKey(Reyting, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class BlogCategory(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class BlogAndPost(models.Model):
    title = models.CharField(max_length=256)
    creator = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    created_at = models.TimeField(auto_now_add=True)
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=False)
    short_description = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.title


class Suggestions(models.Model):
    recipe_id = models.ForeignKey(Recipes,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=100, null=False)
    subject = models.TextField(blank=True)
    message = models.TextField(blank=True)
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name

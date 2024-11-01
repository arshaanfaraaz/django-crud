from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def home(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
        )
        return redirect("/")

    queryset = Recipe.objects.all()
    if request.GET.get("search"):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get("search"))

    context = {"recipex": queryset}

    return render(request, "homepage.html", context)


def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()

    return redirect("/")


def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get("recipe_image")
        recipe_description = data.get("recipe_description")
        recipe_name = data.get("recipe_name")

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect("/")

    context = {"recipe": queryset}
    return render(request, "update-recipes.html", context)

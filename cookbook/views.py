from django.shortcuts import get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe, Product, RecipeProduct


class AddProductToRecipeView(View):
    def get(self, request, recipe_id, product_id, weight):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        product = get_object_or_404(Product, id=product_id)

        recipe_product, created = RecipeProduct.objects.get_or_create(
            recipe=recipe,
            product=product,
            defaults={"weight": weight}
        )

        if not created:
            recipe_product.weight = weight
            recipe_product.save()

        return HttpResponse(f"Product {product.title} added to recipe {recipe.title} with weight {weight}.")


class CookRecipeView(View):
    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        products = recipe.products.all()

        for product in products:
            product.used_counter += 1
            product.save()

        return HttpResponse(f"Recipes cooked for recipe {recipe.title}.")


class ShowRecipesWithoutProductView(View):
    template_name = "cookbook/recipes_without_product.html"

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        recipes_without_product = Recipe.objects.exclude(products=product).filter(
            products__recipeproduct__weight__gte=10)

        context = {"recipes": recipes_without_product}
        return render(request, self.template_name, context)

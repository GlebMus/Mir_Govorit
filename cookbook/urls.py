from django.urls import path
from .views import AddProductToRecipeView, CookRecipeView, ShowRecipesWithoutProductView

app_name = "cookbook"


urlpatterns = [
    path("add_product_to_recipe/<int:recipe_id>/<int:product_id>/<int:weight>/", AddProductToRecipeView.as_view(), name="add_product_to_recipe"),
    path("cook_recipe/<int:recipe_id>/", CookRecipeView.as_view(), name="cook_recipe"),
    path("show_recipes_without_product/<int:product_id>/", ShowRecipesWithoutProductView.as_view(), name="show_recipes_without_product"),
]
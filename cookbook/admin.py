from django.contrib import admin
from .models import Product, Recipe, RecipeProduct


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'used_counter', 'slug']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeProductInline]
    list_display = ('title', 'display_products', 'slug')

    def display_products(self, obj):
        return ', '.join([product.title for product in obj.products.all()])

    display_products.short_description = 'Products'

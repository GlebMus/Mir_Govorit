from django.db import models


class Product(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название продукта",
        unique=True
    )
    used_counter = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество использований"
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name="URl",
    )

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название рецепта"
    )

    products = models.ManyToManyField(
        Product,
        through="RecipeProduct",
        verbose_name="Продукты в рецепте"
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name="URl",
    )

    def __str__(self):
        return self.title


class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name="Рецепт")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    weight = models.PositiveIntegerField(verbose_name="Вес в граммах")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["recipe", "product"], name="unique recipes and products")
        ]

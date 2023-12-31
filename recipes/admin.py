from django.contrib import admin

from recipes.models import Recipe, Ingredient, Step, Tag

# Register your models here.
@admin.register(Recipe)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'dificulty', 'likes', 'bookmarks',]

@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ['recipe', 'step',]

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['recipe', 'quantity', 'description',]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
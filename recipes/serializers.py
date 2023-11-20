from rest_framework import serializers

from recipes.models import Recipe, Ingredient, Step, ImageRecipe

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
        read_only_fields = ['recipe']

class RecipeSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ['user', 'likes', 'bookmarks',]

class RecipesRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'user', 'title', 'description', 'dificulty', 'prep_time',
            'cook_time', 'bill_spent', 'tags', 'likes','bookmarks',
        ]

class ImageRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageRecipe
        fields = '__all__'

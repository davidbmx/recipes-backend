from rest_framework import serializers

from recipes.models import Recipe, Ingredient, Step

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)
    ingredients = IngredientSerializer(many=True)
    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ['user', 'likes', 'bookmarks', 'steps', 'ingredients',]

class RecipesRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'user', 'title', 'description', 'dificulty', 'prep_time',
            'cook_time', 'bill_spent', 'tags', 'likes','bookmarks',
        ]

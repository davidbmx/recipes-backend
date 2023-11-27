from rest_framework import serializers

from recipes.models import Recipe, Ingredient, Step, Tag
from users.serializers import UserPublicSerializer

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

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
    liked = serializers.SerializerMethodField('get_liked')
    bookmarked = serializers.SerializerMethodField('get_bookmarked')
    user = UserPublicSerializer(many=False, read_only=True)
    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ['user', 'likes', 'bookmarks',]

    def get_liked(self, obj):
        user = self.context['request'].user
        if not user.is_authenticated:
            return False
        return obj.like_recipes.filter(user=user).first() != None
    
    def get_bookmarked(self, obj):
        user = self.context['request'].user
        if not user.is_authenticated:
            return False
        return obj.bookmark_recipes.filter(user=user).first() != None

class RecipesRetrieveSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True)
    liked = serializers.SerializerMethodField('get_liked')
    bookmarked = serializers.SerializerMethodField('get_bookmarked')
    class Meta:
        model = Recipe
        fields = [
            'user', 'title', 'description', 'dificulty', 'prep_time',
            'cook_time', 'bill_spent', 'tags', 'likes','bookmarks',
            'steps', 'ingredients', 'liked', 'bookmarked', 'image', 
        ]

    def get_liked(self, obj):
        user = self.context['request'].user
        if not user.is_authenticated:
            return False
        return obj.like_recipes.filter(user=user).first() != None
    
    def get_bookmarked(self, obj):
        user = self.context['request'].user
        if not user.is_authenticated:
            return False
        return obj.bookmark_recipes.filter(user=user).first() != None


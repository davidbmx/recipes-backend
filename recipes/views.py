from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from recipes.serializers import RecipeSerializer, RecipesRetrieveSerializer, IngredientSerializer, StepSerializer
from recipes.models import Recipe, Step, Ingredient
from utils.permissions import IsUserOwner, IsUserRecipe

class RecipeViewset(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    permissions_classes = [IsAuthenticatedOrReadOnly, IsUserOwner]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RecipesRetrieveSerializer
        return self.serializer_class
    
class StepViewset(viewsets.ModelViewSet):
    serializer_class = StepSerializer
    queryset = Step.objects.all()
    permission_classes = ['IsAuthenticated', IsUserRecipe]

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(recipe__user=self.request.user)
        return self.queryset
    
class IngredientViewset(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = ['IsAuthenticated', IsUserRecipe]

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(recipe__user=self.request.user)
        return self.queryset
    
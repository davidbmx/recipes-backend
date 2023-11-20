from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from recipes.serializers import RecipeSerializer, RecipesRetrieveSerializer, IngredientSerializer, StepSerializer, ImageRecipeSerializer
from recipes.models import Recipe, Step, Ingredient, ImageRecipe
from utils.permissions import IsUserOwner, IsUserRecipe

class MixinsRecipe(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(recipe__user=self.request.user)
        return self.queryset
    
    def get_object_recipe(self):
        recipe_id = self.kwargs['recipe_id']
        return get_object_or_404(Recipe, pk=recipe_id, user=self.request.user)

    def get_object(self):
        recipe = self.get_object_recipe()
        print(recipe)
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'], recipe__id = recipe.id)
        self.check_object_permissions(self.request, obj)
        return obj
    
    def list(self, request, *args, **kwargs):
        recipe = self.get_object_recipe()
        queryset = self.get_queryset().filter(recipe=recipe)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        recipe = self.get_object_recipe()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(recipe=recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class RecipeViewset(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    permissions_classes = [IsAuthenticatedOrReadOnly, IsUserOwner]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RecipesRetrieveSerializer
        return self.serializer_class
    
    def get_permissions(self):
        permissions = self.permission_classes
        if self.action == 'create':
            permissions += [IsAuthenticated]
        return [permission() for permission in permissions]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class StepViewset(MixinsRecipe):
    serializer_class = StepSerializer
    queryset = Step.objects.all()
    permission_classes = [IsAuthenticated, IsUserRecipe]

class IngredientViewset(MixinsRecipe):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = [IsAuthenticated, IsUserRecipe]

class ImageRecipesViewset(MixinsRecipe):
    serializer_class = ImageRecipeSerializer
    queryset = ImageRecipe.objects.all()
    permission_classes = [IsAuthenticated, IsUserRecipe]

    
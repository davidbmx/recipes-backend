from django.urls import path
from rest_framework import routers

from recipes.views import RecipeViewset, IngredientViewset, StepViewset, TagsListView

router = routers.DefaultRouter()

router.register(r'recipes', RecipeViewset)
router.register(r'recipes/tags', TagsListView)
router.register(r'recipes/(?P<recipe_id>\d+)/steps', StepViewset)
router.register(r'recipes/(?P<recipe_id>\d+)/ingredients', IngredientViewset)

urlpatterns = router.urls

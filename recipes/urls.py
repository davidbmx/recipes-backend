from rest_framework import routers

from recipes.views import RecipeViewset, IngredientViewset, StepViewset

router = routers.DefaultRouter()

router.register(r'recipes', RecipeViewset)
router.register(r'recipes/steps', StepViewset)
router.register(r'recipes/ingredients', IngredientViewset)

urlpatterns = router.urls

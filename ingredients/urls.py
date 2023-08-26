from django.urls import path
from .views import IngredientsList, IngredientsDetail

app_name = 'ingredients'

urlpatterns = [
    path('ingredients/list', IngredientsList.as_view(), name='ing'),
    path('ingredients/list/<pk>', IngredientsDetail.as_view(), name = 'ingd' )
]
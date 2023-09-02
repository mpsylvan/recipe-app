from django.urls import path
from .views import home, records, RecipeList, RecipeDetail, recipe_input

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home' ),
    path('list', RecipeList.as_view(), name='recipe-list'),
    path('list/<pk>', RecipeDetail.as_view(), name = 'detail' ),
    path('records', records, name='records'),
    path('input', recipe_input, name='recipe-input')
]
from django.urls import path
from .views import home, RecipeList, RecipeDetail

app_name = 'recipes'

urlpatterns = [
    path('', home ),
    path('list', RecipeList.as_view(), name='recipe-list'),
    path('list/<pk>', RecipeDetail.as_view(), name = 'detail' )
]
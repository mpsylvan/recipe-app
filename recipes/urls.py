from django.urls import path
from .views import home, about, records, RecipeList, RecipeDetail, RecipeInput

app_name = "recipes"

urlpatterns = [
    path("", home, name="home"),
    path("about", about, name="about"),
    path("list", RecipeList.as_view(), name="recipe-list"),
    path("list/<pk>", RecipeDetail.as_view(), name="detail"),
    path("records", records, name="records"),
    path("recipe/new", RecipeInput.as_view(), name="recipe-input"),
]

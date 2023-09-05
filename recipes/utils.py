from .models import Recipe
from io import BytesIO
import base64
import matplotlib.pyplot as plt


def get_book_title_from_id(id):
    recipe_ref = Recipe.objects.get(id=id)
    return recipe_ref


def get_graph():
    # create a byte stream for image
    buffer = BytesIO()
    # creates a plot with a bytesio object as a file-like object, Sets the formatting of image to png.
    plt.savefig(buffer, format="png")
    # set cursor to the stream's begin
    buffer.seek(0)
    # get file contents
    image_png = buffer.getvalue()
    # encode our bytestream file
    graph = base64.b64encode(image_png)
    # decode
    graph = graph.decode("utf-8")
    # close the stream and free up mem
    buffer.close()
    return graph


def get_chart(chart_type, data, **kwargs):
    # AntiGrain Geometry
    plt.switch_backend("AGG")
    plt.figure(figsize=(8, 5))
    if chart_type == "a":
        plt.plot(data["name"], data["cooking_time"])
        plt.title("Recipes vs Cooking Times (mins)")
        plt.xticks(rotation=45)
    elif chart_type == "b":
        # pie chart based upon price
        labels = kwargs.get("labels")
        plt.title(f"Ingredient and the % of recipes in the search that contains it ")
        plt.pie(data["recipes_in"], labels=labels, autopct="%1.1f%%")
    elif chart_type == "c":
        plt.bar(
            x=list(data.index),
            height=data.values,
            width=0.4,
            color=["#e388a7", "#5888a7", "#5ca2a2", "#8c57a3"],
        )
        print("This will be a line.")
    else:
        print("Unknown chart type entered")
    plt.tight_layout()
    chart = get_graph()
    return chart

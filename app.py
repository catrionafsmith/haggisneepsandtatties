from flask import Flask, render_template
# render template allows us to reference or use an external HTML code or script
import json, requests

# creating the app, and letting it know that all the info it needs is in this directory
app = Flask(__name__)

# setting up the route for the app(where the main page will go)
@app.route("/")

# this function uses the render_template function and returns a rendered page using the dinner.html template.
def get_dinners():
    url = "https://www.themealdb.com"
    return render_template("dinner.html", url=url)

# this function uses the API to get a random recipe, and then returns the recipe's title, image and link.
def get_recipe():
    url = "http://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url).json()
    recipe_title = response['meals'][0]['strMeal']
    recipe_picture = response['meals'][0]['strMealThumb']
    recipe_link = response['meals'][0]['strSource']
    return recipe_title, recipe_picture, recipe_link


@app.route("/whatsfordinner")

# this function generates and uses variables from the get_recipe() function to render a page on whatsfordinner.html template
def whatsfor():
    recipe_title, recipe_picture, recipe_link = get_recipe()
    return render_template("whatsfordinner.html", recipe_title = recipe_title, recipe_picture=recipe_picture, recipe_link=recipe_link)


if __name__ == "__main__":
    app.run(debug=True)
    # could add in app.run(host="0.0.0.0", port=80) if we need to change the port
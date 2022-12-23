from flask import Flask, render_template
# render template allows us to reference or use an external HTML code or script
import urllib.request, json, requests

import os
# creating the app, and letting it know that all the info it needs is in this directory
app = Flask(__name__)

# setting up the route for the app(where the main page will go)
@app.route("/")
# this function uses the API to get a random meal, and then returns a rendered page.
def get_dinners():
    url = "http://www.themealdb.com/api/json/v1/1/random.php"
    # response = requests.get(url)
    # # response = urllib.request.urlopen(url)
    # data = response.read()
    # dict = json.loads(data)
    dict = requests.get(url).json()
    print(dict)
# where has meals_in come from? can we just pass the whole dict in?
    return render_template("dinner.html", dinners=dict["meals_in"])

def get_recipe():
    url = "http://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url).json()
    recipe_title = response['meals'][0]['strMeal']
    recipe_picture = response['meals'][0]['strMealThumb']
    recipe_link = response['meals'][0]['strSource']
    return recipe_title, recipe_picture, recipe_link

@app.route("/whatsfordinner")
def whatsfor():
    recipe_title, recipe_picture, recipe_link = get_recipe()
    return render_template("whatsfordinner.html", recipe_title = recipe_title, recipe_picture=recipe_picture, recipe_link=recipe_link)

# print(dict)

@app.route("/meals")
def get_meals_list():
    url = "http://www.themealdb.com/api/json/v1/1/random.php"

    dict = requests.get(url).json()

    meals = []

    for meal in dict["meals"]:
        meal = {
            "name": meal["strMeal"],
            "picture":meal["strMealThumb"],
            "recipe": meal["strInstructions"],
        }
        
        meals.append(meal)
    # return render_template ("dinner.html", dinners=dict["meals_in"])
    return {"meals_in": meals}

@app.route("/dinnertime")
def get_dinnertime():
    url = "http://www.themealdb.com/api/json/v1/1/random.php"

    dict = requests.get(url).json()

    meals = []

    for meal in dict["meals"]:
        meal = {
            "name": meal["strMeal"],
            "picture":meal["strMealThumb"],
            "recipe": meal["strInstructions"],
        }
        
        meals.append(meal)
    return render_template("meal_option.html", dinners=dict["meals"])
    # return {"meals_in": meals}

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"



if __name__ == "__main__":
    app.run(debug=True)
    # could add in app.run(host="0.0.0.0", port=80) if we need to change the port
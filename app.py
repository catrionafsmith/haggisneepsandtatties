from flask import Flask, render_template
import urllib.request, json, requests

import os
app = Flask(__name__)
@app.route("/")
def get_dinners():
    url = "http://www.themealdb.com/api/json/v1/1/random.php"
    # response = requests.get(url)
    # # response = urllib.request.urlopen(url)
    # data = response.read()
    # dict = json.loads(data)
    dict = requests.get(url).json()

    return render_template ("dinner.html", dinners=dict["meals_in"])

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
    return render_template ("meal_option.html", dinners=dict["meals"])
    # return {"meals_in": meals}

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


# @app.route("/")
# def index():
#     return "<h1>Homepage!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
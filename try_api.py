import requests
import json

url = "http://www.themealdb.com/api/json/v1/1/random.php"
# response = json.loads(requests.request("GET", url).text)
response = requests.get(url).json()
recipe_title = response['meals'][0]['strMeal']
recipe_picture = response['meals'][0]['strMealThumb']
recipe_link = response['meals'][0]['strSource']
recipe_instructions = response['meals'][0]['strInstructions']

print(response['meals'][0]['strSource'])

# print(dict)
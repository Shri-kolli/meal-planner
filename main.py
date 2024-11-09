from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Sample lists
breakfast_items = ['Pancakes', 'Oatmeal', 'Smoothie']
lunch_items = ['Salad', 'Sandwich', 'Sushi']
dinner_items = ['Pizza', 'Pasta', 'Stir-fry']

# Function to generate a random meal plan
def generate_meal_plan():
    meals = {
        'Monday': {},
        'Tuesday': {},
        'Wednesday': {},
        'Thursday': {},
        'Friday': {},
        'Saturday': {},
        'Sunday': {}
    }

    for day in meals:
        meals[day]['Breakfast'] = random.choice(breakfast_items)
        meals[day]['Lunch'] = random.choice(lunch_items)
        meals[day]['Dinner'] = random.choice(dinner_items)
    
    return meals

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    meal_plan = generate_meal_plan()
    return render_template('result.html', meal_plan=meal_plan)

if __name__ == '__main__':
    app.run(debug=True)

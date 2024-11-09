from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.secret_key = 'mini@1357'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mealplans.db'
db = SQLAlchemy(app)

# Sample lists
breakfast_items = ['dosa', 'idli', 'avalakki', 'uppittu', 'cornflakes & fruits', 'shavige-uppittu', 'bread-uppittu']
main_meals_items = ['brinjal/cut-badane-kayi', 'capsicum', 'cabbage', 'hiri-kayi', 'bhendi', 'beans', 'brinjal/cut-badane-kayi', 'pitla', 'kalu-palya', 'udara-bele', 'kalu-palya']

# 4-digit PIN
PIN = '1357'

class MealPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_data = db.Column(db.PickleType, nullable=False)

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

    used_main_meals = {item: 0 for item in main_meals_items}

    for day in meals:
        meals[day]['Breakfast'] = random.choice(breakfast_items)

        # Ensure no item appears more than twice a week and not repeated on the same day
        lunch_item = None
        while not lunch_item or used_main_meals[lunch_item] >= 2:
            lunch_item = random.choice(main_meals_items)
        meals[day]['Lunch'] = lunch_item
        used_main_meals[lunch_item] += 1

        dinner_item = None
        while not dinner_item or dinner_item == lunch_item or used_main_meals[dinner_item] >= 2:
            dinner_item = random.choice(main_meals_items)
        meals[day]['Dinner'] = dinner_item
        used_main_meals[dinner_item] += 1
    
    return meals

@app.route('/')
def index():
    meal_plan_entry = MealPlan.query.first()
    meal_plan = meal_plan_entry.meal_data if meal_plan_entry else None
    return render_template('index.html', meal_plan=meal_plan)

@app.route('/generate', methods=['POST'])
def generate():
    entered_pin = request.form['pin']
    if entered_pin == PIN:
        meal_plan = generate_meal_plan()
        existing_plan = MealPlan.query.first()
        if existing_plan:
            existing_plan.meal_data = meal_plan
        else:
            new_plan = MealPlan(meal_data=meal_plan)
            db.session.add(new_plan)
        db.session.commit()  # Store the meal plan in the database
        return render_template('index.html', meal_plan=meal_plan)
    else:
        return 'Invalid PIN. Please try again.'

if __name__ == '__main__':
    app.run(debug=True)

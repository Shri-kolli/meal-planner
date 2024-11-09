# from flask import Flask, render_template, request, session, redirect, url_for
# import random

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # Sample lists
# breakfast_items = ['dosa', 'idli', 'avalakki', 'uppittu', 'cornflakes &fruits', 'shavige-uppittu', 'bread-uppittu']
# lunch_items = ['brinjal', 'capsicum', 'Sushi']
# dinner_items = ['Pizza', 'Pasta', 'Stir-fry']

# # 4-digit PIN
# PIN = '1357'

# # Function to generate a random meal plan
# def generate_meal_plan():
#     meals = {
#         'Monday': {},
#         'Tuesday': {},
#         'Wednesday': {},
#         'Thursday': {},
#         'Friday': {},
#         'Saturday': {},
#         'Sunday': {}
#     }

#     for day in meals:
#         meals[day]['Breakfast'] = random.choice(breakfast_items)
#         meals[day]['Lunch'] = random.choice(lunch_items)
#         meals[day]['Dinner'] = random.choice(dinner_items)
    
#     return meals

# @app.route('/')
# def index():
#     meal_plan = session.get('meal_plan')  # Retrieve the meal plan from session if it exists
#     return render_template('index.html', meal_plan=meal_plan)

# @app.route('/generate', methods=['POST'])
# def generate():
#     entered_pin = request.form['pin']
#     if entered_pin == PIN:
#         meal_plan = generate_meal_plan()
#         session['meal_plan'] = meal_plan  # Store the meal plan in session
#         return render_template('result.html', meal_plan=meal_plan)
#     else:
#         return 'Invalid PIN. Please try again.'

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample lists
breakfast_items = ['dosa', 'idli', 'avalakki', 'uppittu', 'cornflakes &fruits', 'shavige-uppittu', 'bread-uppittu']
main_meals_items = ['brinjal/cut-badane-kayi', 'capsicum', 'cabbage', 'hiri-kayi', 'bhendi', 'beans', 'brinjal/cut-badane-kayi', 'pitla', 'kalu-palya', 'udara-bele', 'kalu-palya']

# 4-digit PIN
PIN = '1357'

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
        meals[day]['Lunch'] = random.choice(main_meals_items)
        meals[day]['Dinner'] = random.choice(main_meals_items)
    
    return meals

@app.route('/')
def index():
    meal_plan = session.get('meal_plan')  # Retrieve the meal plan from session if it exists
    return render_template('index.html', meal_plan=meal_plan)

@app.route('/generate', methods=['POST'])
def generate():
    entered_pin = request.form['pin']
    if entered_pin == PIN:
        meal_plan = generate_meal_plan()
        session['meal_plan'] = meal_plan  # Store the meal plan in session
        return render_template('result.html', meal_plan=meal_plan)
    else:
        return 'Invalid PIN. Please try again.'

if __name__ == '__main__':
    app.run(debug=True)

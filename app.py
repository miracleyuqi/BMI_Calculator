
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Declare three constants for value validation
MIN_HEIGHT = 24.0
MAX_HEIGHT = 120.0
MIN_WEIGHT = 25.0
CONVERSION_FACTOR = 703  # Set up a constant for conversion factor.

# BMI Range Constants
BMI_SEVERELY_UNDER = 16
BMI_UNDER = 18.5
BMI_HEALTHY = 25
BMI_OVER = 30

# Utility functions for validation
def valid_height(height):
    try:
        value = float(height)
        return MIN_HEIGHT <= value <= MAX_HEIGHT
    except ValueError:
        return False

def valid_weight(weight):
    try:
        value = float(weight)
        return value >= MIN_WEIGHT
    except ValueError:
        return False

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = (float(weight) / (float(height) ** 2)) * CONVERSION_FACTOR
    return bmi

# Function to determine BMI category
def bmi_category(bmi):
    if bmi < BMI_SEVERELY_UNDER:
        return "severely underweight"
    elif BMI_SEVERELY_UNDER <= bmi < BMI_UNDER:
        return "underweight"
    elif BMI_UNDER <= bmi < BMI_HEALTHY:
        return "healthy"
    elif BMI_HEALTHY <= bmi < BMI_OVER:
        return "overweight"
    else:
        return "obese"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract data from form
        height = request.form.get('height')
        weight = request.form.get('weight')

        # Validate form data
        if not valid_height(height):
            flash('Invalid height. Please enter a value between 24 and 120 inches.')
            return redirect(url_for('index'))
        elif not valid_weight(weight):
            flash('Invalid weight. Please enter a weight of at least 25 pounds.')
            return redirect(url_for('index'))

        # Calculate BMI
        bmi_value = calculate_bmi(weight, height)
        category = bmi_category(bmi_value)

        return render_template('result.html', bmi=round(bmi_value, 1), category=category)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

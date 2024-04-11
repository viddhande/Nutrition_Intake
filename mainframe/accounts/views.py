from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Current
import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder
from .forms import UserInputForm
import numpy as np  # For numerical operations
import joblib

# Load the trained encoder and model


def home(request):
    return render(request, 'index.html')

def success_page(request):
    return render(request, 'mainframe.html')

def index_recipe(request):
    return render(request, 'index_recipe.html')

def sparkle(request):
    return render(request, 'sparkle.html')

def main(request):
    return render(request, 'main.html')

def info(request):
    if request.method == "POST":
        # Retrieve data from the POST request
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        meals_per_day = request.POST.get('meals_per_day')
        meal_portion_size = request.POST.get('meal_portion_size')
        dietary_preference = request.POST.get('dietary_preference')
        lifestyle_preference = request.POST.get('lifestyle_preference')
        existing_health_condition = request.POST.get('existing_health_condition')
        physical_activity_level = request.POST.get('physical_activity_level')
        existing_allergens = request.POST.get('existing_allergens')
        carbohydrate_intake = request.POST.get('carbohydrate_intake')
        protein_intake = request.POST.get('protein_intake')
        fats_intake = request.POST.get('fats_intake')

        # Create a new instance of Current model with the received data
        current_data = Current.objects.create(
            age=age,
            gender=gender,
            height=height,
            weight=weight,
            meals_per_day=meals_per_day,
            meal_portion_size=meal_portion_size,
            dietary_preference=dietary_preference,
            lifestyle_preference=lifestyle_preference,
            existing_health_condition=existing_health_condition,
            physical_activity_level=physical_activity_level,
            existing_allergens=existing_allergens,
            carbohydrate_intake=carbohydrate_intake,
            protein_intake=protein_intake,
            fats_intake=fats_intake
        )


        return render(request, 'new.html')

    else:
        return render(request, 'info.html')

def mainframe(request):
    return render(request, 'mainframe.html')


'''
def main(request):
    if request.method == "POST":
        form = UserInputForm(request.POST)
        if form.is_valid():
            # Get user input from the form
            dietary_preference = form.cleaned_data['dietary_preference']
            lifestyle = form.cleaned_data['lifestyle']
            health_condition = form.cleaned_data['health_condition']
            existing_allergies = form.cleaned_data['existing_allergies']

 # Convert string inputs to numerical values
            dietary_preference_num = convert_to_numeric('DietaryPreference', dietary_preference)
            lifestyle_num = convert_to_numeric('LifestylePreference', lifestyle)
            health_condition_num = convert_to_numeric('HealthCondition', health_condition)
            existing_allergies_num = convert_to_numeric('ExistingAllergies', existing_allergies)


            # Prepare input data for prediction
            input_data = np.array([[dietary_preference_num, lifestyle_num, health_condition_num, existing_allergies_num]])

            # Make prediction using the ML model
            prediction = make_prediction(input_data)

            # Pass prediction to the template
            return render(request, 'new.html', {'output': prediction})

    else:
        form = UserInputForm()
    return render(request, 'main.html', {'form': form})


def convert_to_numeric(column_name, value):
    if column_name == 'DietaryPreference':
        if value == 'Vegetarian':
            return 1
        elif value == 'Non Vegetarian':
            return 2
        elif value == 'Vegan':
            return 3
        else:
            return 0  # Default value or handle other cases as needed

    elif column_name == 'HealthCondition':
        if value == 'Diabetes':
            return 1
        elif value == 'BP':
            return 2
        elif value == 'Hypertension':
            return 3
        else:
            return 0  # Default value or handle other cases as needed

    elif column_name == 'LifestylePreference':
        if value == 'Office Job':
            return 1
        elif value == 'Travel-Oriented':
            return 2
        elif value == 'Settled':
            return 3
        elif value == 'Physical Job':
            return 4
        else:
            return 0  # Default value or handle other cases as needed

    elif column_name == 'ExistingAllergies':
        if value == 'Milk Products':
            return 1
        elif value == 'Soya Products':
            return 2
        elif value == 'Nuts':
            return 3
        elif value == 'Eggs':
            return 4
        else:
            return 0  # Default value or handle other cases as needed




# Load the Random Forest model
#ml_model = joblib.load('random_forest_model (1).sav')

def make_prediction(input_data):
    # Use the loaded ML model to make predictions
    # Input_data should be a 2D array-like object, e.g., a NumPy array
    prediction = ml_model.predict(input_data)
    return prediction
'''


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save()
        return redirect('login')

    else:
        return render(request, 'registration/register.html')

def custom_logout(request):
    logout(request)
    return redirect('home')

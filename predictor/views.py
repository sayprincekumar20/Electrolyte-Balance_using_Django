# from django.shortcuts import render
# from .forms import ElectrolyteForm
# from .models import ElectrolyteData
# import joblib
# import numpy as np

# # Load the model and scaler outside the function for performance
# model = joblib.load('electrolyte_model.pkl')
# scaler = joblib.load('scaler.pkl')

# def predict_electrolyte(request):
#     if request.method == 'POST':
#         form = ElectrolyteForm(request.POST)
#         if form.is_valid():
#             # Get the cleaned data
#             data = form.cleaned_data
#             features = np.array([[data['serum_sodium'], data['serum_potassium'],
#                                    data['serum_calcium'], data['serum_magnesium'],
#                                    data['bicarbonate'], data['phosphorus']]])

#             # Scale the features
#             features_scaled = scaler.transform(features)

#             # Make prediction
#             prediction = model.predict(features_scaled)

#             # Save the data in the database
#             ElectrolyteData.objects.create(
#                 serum_sodium=data['serum_sodium'],
#                 serum_potassium=data['serum_potassium'],
#                 serum_calcium=data['serum_calcium'],
#                 serum_magnesium=data['serum_magnesium'],
#                 bicarbonate=data['bicarbonate'],
#                 phosphorus=data['phosphorus'],
#                 outcome=prediction[0]
#             )

#             return render(request, 'predictor/result.html', {'prediction': prediction[0]})

#     # This section handles both GET requests and failed form submissions
#     else:
#         form = ElectrolyteForm()

#     # Ensure to return a response even if the request method is GET or form is invalid
#     return render(request, 'predictor/predict.html', {'form': form})
from django.shortcuts import render
from .forms import ElectrolyteForm
from .models import ElectrolyteData
import joblib
import pandas as pd

# Load the model and scaler outside the function for performance
model = joblib.load('electrolyte_model.pkl')
scaler = joblib.load('scaler.pkl')

def predict_electrolyte(request):
    if request.method == 'POST':
        form = ElectrolyteForm(request.POST)
        if form.is_valid():
            # Get the cleaned data
            data = form.cleaned_data

            # Create a DataFrame for scaling
            features = pd.DataFrame({
                'Serum Sodium (mmol/L)': [data['serum_sodium']],
                'Serum Potassium (mmol/L)': [data['serum_potassium']],
                'Serum Calcium (mg/dL)': [data['serum_calcium']],
                'Serum Magnesium (mg/dL)': [data['serum_magnesium']],
                'Bicarbonate (mmol/L)': [data['bicarbonate']],
                'Phosphorus (mg/dL)': [data['phosphorus']],
            })

            # Scale the features
            features_scaled = scaler.transform(features)

            # Make prediction
            prediction = model.predict(features_scaled)

            # Save the data in the database
            ElectrolyteData.objects.create(
                serum_sodium=data['serum_sodium'],
                serum_potassium=data['serum_potassium'],
                serum_calcium=data['serum_calcium'],
                serum_magnesium=data['serum_magnesium'],
                bicarbonate=data['bicarbonate'],
                phosphorus=data['phosphorus'],
                outcome=prediction[0]
            )

            return render(request, 'predictor/result.html', {'prediction': prediction[0]})

    # This section handles both GET requests and failed form submissions
    else:
        form = ElectrolyteForm()

    # Ensure to return a response even if the request method is GET or form is invalid
    return render(request, 'predictor/predict.html', {'form': form})

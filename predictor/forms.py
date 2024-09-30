from django import forms

class ElectrolyteForm(forms.Form):
    serum_sodium = forms.FloatField(label='Serum Sodium (mmol/L)')
    serum_potassium = forms.FloatField(label='Serum Potassium (mmol/L)')
    serum_calcium = forms.FloatField(label='Serum Calcium (mg/dL)')
    serum_magnesium = forms.FloatField(label='Serum Magnesium (mg/dL)')
    bicarbonate = forms.FloatField(label='Bicarbonate (mmol/L)')
    phosphorus = forms.FloatField(label='Phosphorus (mg/dL)')

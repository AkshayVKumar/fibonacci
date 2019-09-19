from django import forms

class Form_data(forms.Form):
    Data=forms.IntegerField(min_value=1,help_text="Enter the Integer value",label="Number")
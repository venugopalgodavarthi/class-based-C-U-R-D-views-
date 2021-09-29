from django import forms

# Create your models here.


class empform(forms.Form):
    name= forms.CharField(widget=forms.TextInput)
    email= forms.EmailField(widget=forms.TextInput)
    sal= forms.IntegerField()
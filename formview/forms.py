from django import forms
from formview.models import empmodel
# Create your models here.

class empform(forms.ModelForm):
   class Meta:
       model = empmodel
       fields='__all__'
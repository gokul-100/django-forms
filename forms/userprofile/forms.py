from django import forms
from .models import Review
 
 
class Feedbackform(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__' #['user_name',rating]
        #exclude = []
        labels = {
            'user_name':'Your Name'
        }
 
 
 
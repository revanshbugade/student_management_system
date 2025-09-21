from django import forms
from .models import StudentsModel

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentsModel
        fields=('first_name','last_name','email','phone','course','course_timing')
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'course':forms.Select(attrs={'class':'form-select'}),
            'course_timing': forms.Select(attrs={'class': 'form-select'})
        }



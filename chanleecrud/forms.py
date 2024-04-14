from django import forms

from chanleecrud.models import User, Course


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control',
                'id':'nameid'}),
            'email': forms.EmailInput(attrs={'class':'form-control',
                'id':'emailid'}),
            'password': forms.PasswordInput(attrs={'class':'form-control',
                'id':'passwordid'}),
        }

class CourseRegistration(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control',
                'id':'nameid'}),
            'description': forms.Textarea(attrs={'class':'form-control',
                'id':'descid'}),
        }
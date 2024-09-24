from django import forms 
from django.core import validators 

class TeacherFormregistration(forms.Form):
    frist_name=forms.CharField(label='Enter your frist name',label_suffix=' ')
    last_name=forms.CharField(label="Enter your last name",label_suffix=" ")
    email = forms.EmailField(initial="rakibcse201@gmail.com",label="Enter your email",label_suffix=' ',disabled=True)
    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(widget=forms.PasswordInput)
    textarea=forms.CharField(widget=forms.Textarea)
    File=forms.CharField(widget=forms.FileInput)
    
    
    def clean(self):
        cleaned_data = super().clean()
        rightpassword = self.cleaned_data['password']
        wrongpassword = self.cleaned_data['repassword']
        if rightpassword != wrongpassword:
            raise forms.ValidationError('Password does not matched')
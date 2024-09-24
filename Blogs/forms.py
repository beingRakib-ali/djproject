from django import forms

class TeacherFormregistration(forms.Form):
    frist_name=forms.CharField(label='Enter your frist name')
    last_name=forms.CharField(label="Enter your last name")
    email = forms.EmailField(initial="rakibcse201@gmail.com", disabled=True)
    password=forms.CharField(widget=forms.PasswordInput)
    textarea=forms.CharField(widget=forms.Textarea)
    File=forms.CharField(widget=forms.FileInput)
    
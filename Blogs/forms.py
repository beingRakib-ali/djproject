from django import forms

class TeacherFormregistration(forms.Form):
    frist_name=forms.CharField(label='Enter your frist name',label_suffix=' ')
    last_name=forms.CharField(label="Enter your last name",label_suffix=" ")
    email = forms.EmailField(initial="rakibcse201@gmail.com",label="Enter your email",label_suffix=' ',disabled=True)
    password=forms.CharField(widget=forms.PasswordInput)
    textarea=forms.CharField(widget=forms.Textarea)
    File=forms.CharField(widget=forms.FileInput)
    
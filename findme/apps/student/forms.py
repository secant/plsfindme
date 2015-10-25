from django import forms


# forms can go here

class StudentForm(forms.Form):
    university = forms.CharField(label='university', max_length=200)
    first_name = forms.CharField(label='first_name', max_length=50)
    last_name = forms.CharField(label='last_name', max_length=50)
    email = forms.EmailField(label='email')
    department = forms.CharField(label='department', max_length=150)
    course_number = forms.CharField(label='course_number', max_length=6)
    course_type = forms.CharField(label='course_type', max_length=15)
    section = forms.IntegerField(label='section')
    bio = forms.CharField(label='bio', max_length=500, widget=forms.Textarea(attrs={'cols': 40, 'rows': 7}))
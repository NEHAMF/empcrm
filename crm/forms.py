from django import forms
from crm.models import Employees
class EmployeeForm(forms.Form):
    name=forms.CharField()
    department=forms.CharField()
    salary=forms.IntegerField()
    email=forms.EmailField()
    age=forms.IntegerField()
    contact=forms.CharField()


class EmployeeModelForm(forms.ModelForm):

    class Meta:
        model=Employees 
        fields="__all__"   #set dic to meta class

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "department":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "age":forms.NumberInput(attrs={"class":"form-control"}),
            "contact":forms.Textarea(attrs={"class":"form-control","rows":5})
        }
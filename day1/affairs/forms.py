
from dataclasses import fields
from django import forms
from .models import track , student

class form1(forms.Form):
    name= forms.CharField(max_length=30)
    mail=forms.EmailField()
    bdate=forms.DateField(widget=forms.DateInput(attrs={'class' :"form-control"}) , label='Birth Date')
    address=forms.CharField(max_length=40 , widget=forms.TextInput(attrs={'class' :"form-control"})) 
    track= forms.ChoiceField(choices=[(t.id , t.name) for t in track.objects.all()] )
    
    name.widget.attrs.update({'class' :"form-control"})
    mail.widget.attrs.update({'class':'form-control'})
    track.widget.attrs.update({'class' :"form-select"})



class form2(forms.ModelForm):
    class Meta:
        model= student
        fields='__all__'

from django import forms

class BuatEventForm(forms.Form):
    judul = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    deskripsi = forms.CharField(max_length=5000, widget=forms.Textarea(attrs={'class':'form-control'}))
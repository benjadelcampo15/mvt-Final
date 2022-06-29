from django import forms





class usuarioCrear(forms.Form):
    nombre = forms.CharField(max_length=30)
    mail = forms.EmailField()
    nacimiento = forms.DateField()

class posteoCrear(forms.Form):
    titulo = forms.CharField(max_length=20)
    cuerpo = forms.CharField(max_length=200)    

class moderadorCrear(forms.Form):
    nombre = forms.CharField(max_length=30)
    mail = forms.EmailField()
    sector = forms.CharField(max_length=30)
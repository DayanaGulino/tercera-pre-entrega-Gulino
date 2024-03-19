from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField (max_length = 48, required= True)
    comision = forms.IntegerField(max_value=100, required=True)

class UsuarioForm(forms.Form):
    nombre_agencia = forms.CharField(max_length=48, required= True)
    contraseña = forms.CharField(max_length=100. required= True)

class StaffForm(forms.Form):
    nombre = forms.CharField(max_length=48, required= True)
    apellido = forms.CharField(max_length=48, required= True)
    email = forms.EmailField()

class AgenciaForm(forms.Form):
    nombre = forms.CharField(max_length=48, required= True)
    tipo = forms.CharField(max_length=48, required= True) 
    id = forms.CharField(max_length=10)

class RegistroForm(forms.Form):
    nombre_agencia = forms.CharField(max_length=100, required=True)
    contraseña = forms.CharField(widget=forms.PasswordInput, required=True)
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput, required=True)

class LoginForm(forms.Form):
    nombre_agencia = forms.CharField(max_length=100, required=True)
    contraseña = forms.CharField(widget=forms.PasswordInput, required=True)

 

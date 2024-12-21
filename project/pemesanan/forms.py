from django import forms
from .models import Pemesanan

class PemesananCreationForm(forms.ModelForm):
  class Meta:
    model = Pemesanan
    fields = ['nama_lengkap', 'email', 'alamat']
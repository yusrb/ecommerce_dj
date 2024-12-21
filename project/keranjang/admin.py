from django.contrib import admin
from .models import (
  Keranjang,
  KeranjangItem,
)

# Register your models here.
@admin.register(Keranjang)
class KeranjangAdmin(admin.ModelAdmin):
  pass

@admin.register(KeranjangItem)
class KeranjangItemAdmin(admin.ModelAdmin):
  pass
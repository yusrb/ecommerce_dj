from django.contrib import admin
from .models import (
  Pemesanan,
  PemesananItem,
)

# Register your models here.
class PemesananItemInline(admin.TabularInline):
  model = PemesananItem
  raw_id_fields = ['produk']

@admin.register(Pemesanan)
class PemesananAdmin(admin.ModelAdmin):
  list_display = ('id', 'nama_lengkap', 'email',)
  inlines = [PemesananItemInline]
  readonly_fields = ('dibuat_pada',)
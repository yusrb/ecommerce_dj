from django.contrib import admin
from .models import (
  Kategori,
  Produk
)

# Register your models here.
@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
  list_display = ('nama', 'slug',)
  prepopulated_fields = {
    'slug':('nama',)
  }

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
  list_display = ('nama', 'harga', 'tersedia', 'dibuat_pada', 'diupdate_pada', 'kategori', )
  prepopulated_fields = {
    'slug':('nama',)
  }
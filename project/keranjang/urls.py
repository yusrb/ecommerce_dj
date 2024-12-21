from django.urls import path
from .views import (
  tambah_keranjang,
  detail_keranjang,
  hapus_keranjang,
)

urlpatterns = [
  path('tambah/<int:produk_id>/', tambah_keranjang, name="tambah_keranjang"),
  path('', detail_keranjang, name="detail_keranjang"),
  path('hapus/<int:produk_id>', hapus_keranjang, name="hapus_keranjang"),
]
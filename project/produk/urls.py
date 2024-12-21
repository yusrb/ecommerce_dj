from django.urls import path
from .views import (
  daftar_produk,
  detail_produk
)

urlpatterns = [
  path('', daftar_produk, name="daftar_produk"),
  path('<slug:kategori_slug>', daftar_produk, name="daftar_produk_by_kategori"),
  path('<int:id>/<slug:slug>', detail_produk, name="detail_produk")
]
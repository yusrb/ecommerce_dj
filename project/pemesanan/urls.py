from django.urls import path
from .views import (
  buat_pesanan,
  konfirmasi_pesanan,
)

urlpatterns = [
  path('buat/', buat_pesanan, name="buat_pesanan"),
  path('konfirmasi/<int:pemesanan_id>', konfirmasi_pesanan, name="konfirmasi_pesanan"),
]
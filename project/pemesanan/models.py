from django.db import models
from produk.models import Produk

# Create your models here.
class Pemesanan(models.Model):
  nama_lengkap = models.CharField(max_length=250)
  email = models.EmailField()
  alamat = models.CharField(max_length=250)
  dibuat_pada = models.DateTimeField(auto_now_add=True)
  update_pada = models.DateField(auto_now=True)
  dibayar = models.BooleanField(default=False)

  def get_total_biaya(self):
    return sum(item.get_biaya() for item in self.pemesananitem_set.all())

class PemesananItem(models.Model):
  pesanan = models.ForeignKey(Pemesanan, on_delete=models.CASCADE)
  produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
  harga = models.DecimalField(max_digits=10, decimal_places=2)
  kuantitas = models.PositiveIntegerField(default=1)

  def get_biaya(self):
    return self.harga * self.kuantitas
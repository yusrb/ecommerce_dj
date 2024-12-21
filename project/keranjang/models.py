from django.db import models
from produk.models import Produk

# Create your models here.
class Keranjang(models.Model):
  dibuat_pada = models.DateTimeField(auto_now_add=True)

  def get_total_harga(self):
    return sum(item.get_total_harga() for item in self.keranjangitem_set.all() )

class KeranjangItem(models.Model):
  keranjang = models.ForeignKey(Keranjang, on_delete=models.CASCADE)
  produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
  kuantitas = models.PositiveIntegerField(default=1)

  def get_total_harga(self):
    return self.produk.harga * self.kuantitas
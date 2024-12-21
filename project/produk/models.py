from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Kategori(models.Model):
  nama = models.CharField(max_length=100)
  slug = models.SlugField(unique=True)

  class Meta:
    verbose_name = "Kategori"
    verbose_name_plural = "Kategori"
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.nama)
    super().save(*args, **kwargs)
  def __str__(self):
    return self.nama

class Produk(models.Model):
  kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
  nama = models.CharField(max_length=200)
  slug = models.SlugField()
  deskripsi = models.TextField(blank=True)
  harga = models.DecimalField(max_digits=10, decimal_places=2)
  tersedia = models.BooleanField(default=True)
  dibuat_pada = models.DateTimeField(auto_now_add=True)
  diupdate_pada = models.DateField(auto_now=True)
  gambar = models.ImageField(upload_to="gambar_produk/")

  class Meta:
    verbose_name = "Produk"
    verbose_name_plural = "Produk"

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.nama)
    super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse('produk:produk_detail', kwargs={'id':self.id, 'slug':self.slug})

  def __str__(self):
    return self.nama
from django.shortcuts import render, get_object_or_404 , redirect
from .models import Kategori, Produk

# Create your views here.
def daftar_produk(request, kategori_slug=None):
  kategori = None
  all_produk = Produk.objects.filter(tersedia=True)
  all_kategori = Kategori.objects.all()

  if kategori_slug:
    kategori = get_object_or_404(Kategori, slug=kategori_slug)
    all_produk = all_produk.filter(kategori=kategori)

  context = {
    'kategori': kategori,
    'kategoris': all_kategori,
    'produks': all_produk,
  }

  return render(request, 'produk/daftar_produk.html', context)

def detail_produk(request, id, slug):
  get_produk = get_object_or_404(Produk, id=id, slug=slug, tersedia=True)

  context = {
    'produk': get_produk
  }

  return render(request, 'produk/detail_produk.html', context)
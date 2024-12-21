from django.shortcuts import render, redirect, get_object_or_404
from .forms import PemesananCreationForm
from .models import (
  Pemesanan,
  PemesananItem,
)
from keranjang.models import Keranjang

# Create your views here.
def buat_pesanan(request):
  keranjang = None
  keranjang_id = request.session.get('keranjang_id')

  if keranjang_id:
    keranjang = Keranjang.objects.get(id=keranjang_id)

    if not keranjang or not keranjang.keranjangitem_set.exists():
      return redirect('keranjang:detail_keranjang')

    if request.method == 'POST':
      form = PemesananCreationForm(request.POST)
      if form.is_valid():
        pesanan = form.save(commit=False)
        pesanan.save()

        for item in keranjang.keranjangitem_set.all():
          PemesananItem.objects.create(
            pesanan = pesanan,
            produk = item.produk,
            harga = item.produk.harga,
            kuantitas = item.kuantitas,
          )
        keranjang.delete()
        del request.session['keranjang_id']
        return redirect('pemesanan:konfirmasi_pesanan', pesanan.id)
    else:
      form = PemesananCreationForm()

    context = {
      'keranjang': keranjang,
      'form': form,
    }

    return render(request, 'pemesanan/buat_pemesanan.html', context)

def konfirmasi_pesanan(request, pemesanan_id):
  pesanan = get_object_or_404(Pemesanan, id=pemesanan_id)

  context = {
    'pesanan': pesanan
  }

  return render(request, 'pemesanan/konfirmasi_pemesanan.html', context)
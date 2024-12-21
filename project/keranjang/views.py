from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from produk.models import Produk
from .models import (
  Keranjang,
  KeranjangItem,
)

# Create your views here.
@require_POST
def tambah_keranjang(request, produk_id):
    keranjang_id = request.session.get('keranjang_id')

    if keranjang_id:
        try:
            keranjang = Keranjang.objects.get(id=keranjang_id)
        except Keranjang.DoesNotExist:
            keranjang = Keranjang.objects.create()
            request.session['keranjang_id'] = keranjang.id
    else:
        keranjang = Keranjang.objects.create()
        request.session['keranjang_id'] = keranjang.id

    produk = get_object_or_404(Produk, id=produk_id)

    keranjang_item, created = KeranjangItem.objects.get_or_create(keranjang=keranjang, produk=produk)

    if not created:
        keranjang_item.kuantitas += 1

    keranjang_item.save()

    response_data = {
        'success': True,
        'message': f'Menambah {produk.nama} ke Keranjang.'
    }

    return JsonResponse(response_data)

def detail_keranjang(request):
    keranjang_id = request.session.get('keranjang_id')
    keranjang = None

    if keranjang_id:
        try:
            keranjang = Keranjang.objects.get(id=keranjang_id)
        except Keranjang.DoesNotExist:
            keranjang = None

    context = {
        'keranjang': keranjang,
    }
    return render(request, 'keranjang/detail_keranjang.html', context)

def hapus_keranjang(request, produk_id):
  keranjang_id = request.session.get('keranjang_id')
  keranjang = get_object_or_404(Keranjang, id=keranjang_id)
  item = get_object_or_404(KeranjangItem, id=produk_id)
  item.delete()

  return redirect('keranjang:detail_keranjang')
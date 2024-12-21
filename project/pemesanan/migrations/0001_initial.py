# Generated by Django 5.1.4 on 2024-12-21 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pemesanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('alamat', models.CharField(max_length=250)),
                ('dibuat_pada', models.DateTimeField(auto_now_add=True)),
                ('update_pada', models.DateField(auto_now=True)),
                ('dibayar', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PemesananItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kuantitas', models.PositiveIntegerField(default=1)),
                ('pesanan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pemesanan.pemesanan')),
                ('produk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produk.produk')),
            ],
        ),
    ]
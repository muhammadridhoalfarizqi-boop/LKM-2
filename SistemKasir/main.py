from sistem_kasir import Produk, Keranjang

p1 = Produk("Kopi Kenangan",   25000,  stok=10)
p2 = Produk("Susu UHT",        18000,  stok=5)
p3 = Produk("Keyboard Gaming", 250000, stok=3)
p4 = Produk("Charger Palsu",   15000,  stok=0)

keranjang_saya = Keranjang(pelanggan_member=True)

keranjang_saya.tambah_produk(p1, jumlah=2)
keranjang_saya.tambah_produk(p2, jumlah=1)
keranjang_saya.tambah_produk(p3, jumlah=1)
keranjang_saya.tambah_produk(p4, jumlah=1) 

keranjang_saya.hapus_produk("Susu UHt")

keranjang_saya.bayar(uang_diterima=400000)
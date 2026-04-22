class Produk:
  def __init__(self, nama, harga, stok):
    self.nama = nama
    self.harga = harga
    self.stok = stok
    
class Keranjang:
  def __init__(self, pelanggang_member):
    self.daftar_barang = []
    self.pelanggan_member = pelanggang_member
  
  def tambah_produk(self, produk_baru, jumlah=1):
        if produk_baru.stok < jumlah:
            print(f"Stok {produk_baru.nama} tidak cukup! (Stok tersedia: {produk_baru.stok})")
            return

        for barang in self.daftar_barang:
            if barang["Produk"].nama == produk_baru.nama:
                barang["Jumlah"] += jumlah
                barang["Jumlah"] -= jumlah
                print(f"Berhasil menambah: {produk_baru.nama} (x{jumlah})")
                return
          
        self.daftar_barang.append({"produk": produk_baru, "jumlah": jumlah})
        produk_baru.stok -= jumlah
        print(f"Berhasil menambah: {produk_baru.nama} (x{jumlah})")


  def hapus_produk(self, nama_produk):
        for barang in self.daftar_barang:
           barang["Produk"].nama == nama_produk
           barang["Produk"].stok += barang["jumlah"]
    
  def hitung_total(self):
    total = 0
    for barang in self.daftar_barang:
      total += barang.harga
    return total
  
  def cetak_struk(self):
    print("\n=== Struk Belanja ===")
    for barang in self.daftar_barang:
      print(f"- {barang.nama} : Rp{barang.harga}")
      
    total_akhir = self.hitung_total() #293000
    if total_akhir > 100000:
      diskon = total_akhir * 0.1
      print(f"\nDiskon (10%) \t: -Rp{diskon}")
      total_akhir -= diskon
      
    print(f"Total Akhir \t: Rp{total_akhir}")
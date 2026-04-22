class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

class Keranjang:
    def __init__(self, is_member=False):
        self.daftar_barang = []
        self.is_member = is_member

    def tambah_produk(self, produk_baru, jumlah=1):
        if jumlah > produk_baru.stok:
            print(f"Stok {produk_baru.nama} tidak cukup! Stok tersedia: {produk_baru.stok}")
            return
        for item in self.daftar_barang:
            if item['produk'].nama == produk_baru.nama:
                if item['jumlah'] + jumlah > produk_baru.stok:
                    print(f"Stok {produk_baru.nama} tidak cukup!")
                    return
                item['jumlah'] += jumlah
                print(f"Berhasil menambah: {produk_baru.nama} (x{jumlah})")
                return
        self.daftar_barang.append({'produk': produk_baru, 'jumlah': jumlah})
        print(f"Berhasil menambah: {produk_baru.nama} (x{jumlah})")

    def hapus_produk(self, nama_produk):
        for item in self.daftar_barang:
            if item['produk'].nama == nama_produk:
                self.daftar_barang.remove(item)
                print(f"Berhasil menghapus: {nama_produk}")
                return
        print(f"Produk '{nama_produk}' tidak ditemukan.")

    def hitung_total(self):
        total = 0
        for item in self.daftar_barang:
            total += item['produk'].harga * item['jumlah']
        return total

    def bayar(self, uang_diterima):
        total = self._hitung_total_akhir()
        if uang_diterima < total:
            print(f"Uang tidak cukup! Kekurangan: Rp{total - uang_diterima:,.0f}")
            return
        print(f"Uang Diterima : Rp{uang_diterima:,.0f}")
        print(f"Kembalian : Rp{uang_diterima - total:,.0f}")
        print("Transaksi Berhasil!")

    def _hitung_total_akhir(self):
        total = self.hitung_total()
        if total > 100000:
            total -= total * 0.1
        if self.is_member:
            total -= total * 0.05
        total += total * 0.11
        return total

    def cetak_struk(self):
        print("\n=== Struk Belanja ===")
        for item in self.daftar_barang:
            subtotal = item['produk'].harga * item['jumlah']
            print(f"- {item['produk'].nama} ({item['jumlah']}x) : Rp{subtotal:,.0f}")

        print("--------------------")
        subtotal = self.hitung_total()
        total = subtotal
        print(f"Subtotal : Rp{subtotal:,.0f}")

        if subtotal > 100000:
            diskon = subtotal * 0.1
            total -= diskon
            print(f"Diskon 10% : -Rp{diskon:,.0f}")

        if self.is_member:
            diskon_member = total * 0.05
            total -= diskon_member
            print(f"Diskon Member 5%: -Rp{diskon_member:,.0f}")
        else:
            print(f"Member : Tidak Aktif")

        ppn = total * 0.11
        total += ppn
        print(f"PPN 11% : +Rp{ppn:,.0f}")
        print("====================")
        print(f"Total Akhir : Rp{total:,.0f}")
        print("====================")
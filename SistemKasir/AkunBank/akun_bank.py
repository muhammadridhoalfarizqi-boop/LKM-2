class AkunBank:
  def __init__(self, nomor, pemilik, saldo_awal):
    self.nomor = nomor 
    self.pemilik = pemilik
    self.saldo = saldo_awal
    self.riwayat = []

  def cek_saldo(self):
    print(f"Saldo {self.pemilik}: Rp{self.saldo}")
    
  def tarik_tunai(self, jumlah):
    if jumlah <= 0:
        print("Jumlah Penarikan harus lebih dari 0!")
        return
    
    if jumlah <= self.saldo:
      self.saldo -= jumlah
      pesan = f"Tarik tunai Rp{jumlah:,}"
      print(f"{self.pemilik} menarik Rp{jumlah:,}") # Ketentuan 3 : simpan ke riwayat
      self.riwayat.append(pesan)
    else:
      print("Saldo tidak cukup!")
  
  def transfer(self, tujuan, jumlah):
      BIAYA_ADMIN = 2500 # Ketentuan 2 : Biaya admin transfer

      if jumlah <= 0:
         print("jumlah transfer harus lebih besar dari 0!")
         return
      
      total_bayar = jumlah + BIAYA_ADMIN

      if self.saldo >= jumlah:
        self.saldo -= jumlah
        tujuan.saldo += jumlah
        pesan = f"Transfer Rp{jumlah} ke {tujuan.pemilik} (biaya admin Rp{BIAYA_ADMIN:,})"
        print(f"Transfer Rp{jumlah:,} ke {tujuan.pemilik} Berhasil!")
        print(f"Biaya admin: Rp{BIAYA_ADMIN:,}")
        self.riwayat.append(pesan)
        tujuan.riwayat.append(
           f"Menerima Transfer Rp{jumlah:,} dari {self.pemilik}"
        )
      else:
        print("Transfer Gagal: Saldo tidak cukup (butuh Rp{total_bayar:,} termasuk biaya admin).")

  def lihat_riwayat(self):
      print(f"\n{'='*40}")
      print(f"  Riwayat Transaksi - {self.pemilik}")
      print(f"\n{'='*40}")
      if len(self.riwayat) == 0:
         print("  Belum ada Transaksi.")
      else:
         for i, transaksi in enumerate(self.riwayat, start=1):
              print(f"  {i}, {transaksi}")
      print(f"\n{'='*40}")  
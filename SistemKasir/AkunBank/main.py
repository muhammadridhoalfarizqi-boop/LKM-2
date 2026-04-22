from akun_bank import AkunBank

akun1 = AkunBank("123", "Hafidz", 200000)
akun2 = AkunBank("234", "Almira", 500000)

akun1.tarik_tunai(0)
akun2.transfer(akun1, -5000)

akun1.tarik_tunai(300000)
akun2.transfer(akun1, 200000)
akun1.tarik_tunai(100000)

akun1.cek_saldo()
akun2.cek_saldo()

akun1.lihat_riwayat()
akun2.lihat_riwayat()
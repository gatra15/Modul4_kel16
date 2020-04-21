class parkiran : 
	#variabel global
	biaya = 0
	
	#fungsi identitas
	def __init__ (self):
		self.masuk = int(input('Jam Masuk\t: '))
		self.keluar = int(input('Jam Keluar\t: '))

	#void-type function
	def hitung(self):
		#insialisasi awal
		harga = 0
		lama = self.keluar - self.masuk
		print('\n\n---------- Jenis Kendaraan ----------')
		print('[1] Motor\n[2] Mobil')
		#kondisi *mengulang jika salah masukkan
		while True :
			pilih = int(input('PILIH JENIS > '))
			if pilih == 1 :
				kendaraan = "Motor"
				harga = 2000
				break
			elif pilih == 2 :
				kendaraan = "Mobil"
				harga = 4000
				break
			else :
				print('[Masukan Anda salah!]')
				

		#menghitung biaya
		biaya = harga * lama
		if biaya > 20000 :
			biaya = 20000
		else :
			biaya = biaya

		print('\n\n--------------- Biaya ---------------')
		print(f"Biaya parkir {kendaraan}   : Rp.",biaya )

		#bayar
		uang = int(input('Uang yang dibayarkan : Rp. '))
		kembalian = uang - biaya
		print('Uang kembalian \t     : Rp.', kembalian)


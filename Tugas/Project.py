import kelas
simpan = [];

def ulang() :
	loop = input('Apakah Anda ingin menghitung lagi?[ya/tidak]\n')
	while (loop == "ya" or loop == "Ya") :
		awal()
	print('Terimakasih!')

def awal():
	print("\n=====================================\n")
	print("-------- Jadwal keluar-masuk --------")
	objek = kelas.parkiran()
	objek.hitung()
	print("\n=====================================\n")

def menu():
	print("=====  Welcome to Our Programs  =====")
	print("===== This is Parking Ticketing =====")

menu()
awal()
ulang()
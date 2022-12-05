#kelas induk = kendaraan , kelas turunan = mobil
#kendaraan mempunyai sifat berjalan(), mobil mempunyai sifat berjalan() tapi lebih spesifik

class kendaraan:
    def berjalan(self):
        print('berjalan')

class mobil(kendaraan):
    def berjalan(self, kecepatan, satuan = 'km/j'):
        print(f'berjalan lebih ngebut {kecepatan} {satuan}')

#instansiasi
sepeda = kendaraan()
sedan = mobil()

sepeda.berjalan()
sedan.berjalan(200)


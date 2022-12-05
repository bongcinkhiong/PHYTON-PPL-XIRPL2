class siswa:
    def __init__(self, nama ):
        self.nama = nama

siswa_nama = siswa('iqbal')
print(f'Siswa kami bernama {siswa_nama.nama}')



class guru:
    def __init__(self, nama):
        self._nama = nama

class sensei(guru):
    def __init__(self, nama, ngajar):
        super().__init__(nama)
        self._ngajar = ngajar

    def ff(self):
        print(f'Guru {self._nama} bernama {self._ngajar}')
manis = sensei('Dava', 'arya')
manis.ff()


class llk:
    def __init__(self, name):
        self.__name = name

    def kepsek(self):
        print(f'Kepsek Arya bernama {self.__name}')
    
pak = llk('Pak Lilik')
pak.kepsek()
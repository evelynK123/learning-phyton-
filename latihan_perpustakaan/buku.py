class Buku:
    def __init__(self, judul, penulis, tahun, status):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.status = status
        
    def info(self):
        print(f"{self.judul} oleh {self.penulis} (___) - {self.status}")
    
    def ubah_status(self, status_baru):
        ______ = status_baru
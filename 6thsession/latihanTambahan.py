#Modularity 

class Buku:
    def __init__(self, judul, penulis, tahun, stok=1):
        
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.stok = stok
        
    def info_buku(self):
        print(f"'{self.judul}', oleh {self.penulis}, tahun {self.tahun}")


# Buku1 = Buku("Outlier", "Gladwell Malcolm", "2008")
# Buku1.info_buku()

# Buku2 = Buku("Nudge", "Richard H. Thaler", "2009")
# Buku2.info_buku()
        
        
#Encapsulation 

class Anggota:
    def __init__(self, nama):
        self.nama = nama
        self.__pinjaman = [] #private list
        
    def pinjam_buku(self, buku):
        if buku.stok > 0: 
            self.__pinjaman.append(buku)
            buku.stok -= 1 #dibenerin chatgpt 
            print(f"{self.nama} berhasil meminjam '{buku.judul}'") 
            
        else:
            print(f"Maaf, stok '{stok.judul}' habis") 
        
    
    def lihat_pinjaman(self):
        if not self.__pinjaman:
            print(f"{self.nama} belum meminjam buku apa pun.")
            
        else:
            print(f"{self.nama} meminjam:") #dibenerin chatgpt 
            for b in self.__pinjaman:
                print("-", {self.__pinjaman})
                
    def kembalikan_buku(self, buku):
        if buku in self.__pinjaman:
            self.__pinjaman.remove(buku)
            buku.stok += 1
            print (f"{self.nama} meminjam: ")
          
        else:
            print(f"{self.nama} tidak meminjam '{buku.judul}'")
            
'''
bingung 
chat gpt to pu stock for learning purposes
'''
    
Anggota1 = Anggota("Evelyn")
Anggota1.lihat_pinjaman() #bingung 

Anggota2 = Anggota("Martha")
Anggota2.lihat_pinjaman()

Anggota3 = Anggota("Rachele")
Anggota3.lihat_pinjaman()
        
# inheritance

class Petugas:
    def __init__(self, nama):
        self.nama = nama

    def info_petugas(self):
        print(f"Petugas: {self.nama}")

class PetugasAdmin(Petugas):
    def kelola_buku(self):
        print(f"{self.nama} sedang mengelola koleksi buku")
        
class PetugasLayanan(Petugas):
    def layani_anggota(self):
        print(f"{self.nama} sedang melayani anggota")
        



#implementasikan alur disini 

admin = PetugasAdmin("Rina")
layanan = PetugasLayanan("Budi")

admin.kelola_buku()
layanan.layani_anggota()
            
# challenge 

def simulasi(): 
    
    Buku1 = Buku("Outlier", "Gladwell Malcolm", 2008, 5)
    Buku1.info_buku()

    Buku2 = Buku("Nudge", "Richard H. Thaler", 2009, 3)
    Buku2.info_buku()
    
    Buku3 = Buku("Atomic Habits", "James Clear", 2018, 1)
    Buku3.info_buku()
    
     
    Anggota1 = Anggota("Evelyn")
    Anggota2 = Anggota("Martha")
    Anggota3 = Anggota("Rachele")
    
    admin = PetugasAdmin("Rina")
    layanan = PetugasLayanan("Budi")

    admin.kelola_buku()
    layanan.layani_anggota()
    
    Anggota1.kembalikan_buku

def menu_perpustakaan():
    daftar_buku = [
        Buku("Outlier", "Gladwell Malcolm", "2008"),
        Buku("Nudge", "Richard H. Thaler", "2009")
    ]
   
Anggota = Anggota("Evelyn")

while True:
    print("\n======= MENU PERPUSTAKAAN ========")
    print("1. Lihat Daftar Buku")
    print("2. Tambahan Buku")
    print("3. Pinjam Buku")
    print("4. Kembalikan Buku")
    print("5. Lihat Buku")
    print("6. Keluar")
    
    pilihan = input("Pilih menu 1-6: ")
    if pilihan == "1":
        print("\n Daftar Buku:")
        for i in enumerate(daftar_buku, 1):
             print(f"{1}. {b.judul} ({b.stok} tersedia)")
             
    elif pilihan == "2":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")
        tahun = input("Tahun terbit: ")
        stok = int(input("Stok awal: "))
        daftar_buku.append(Buku(judul, penulis, tahun, stok))
        print(f"buku '{judul}' berhasil ditambahkan!")
        
    elif pilihan == "3":
        for i, b in enumerate(daftar_buku, 1):
            print(f"{i}. {judul} ({b.stok} tersedia)")
        idx = int(input("Pilih nomor buku:")) - 1
        if  0 <= idx < len(daftar_buku):
            Anggota.pinjam_buku(daftar_buku[idx])
            
    elif pilihan == "4":
        Anggota.lihat_pinjaman()
        judul = input("Masukan judul buku yang dikembalikan: ")
        for b in daftar_buku: 
            if b.judul.lower() == judul.lower():
                if b.judul.lower() == judul.lower():
                    Anggota.kembalikan_buku(b)
                    break
        else:
            print("Buku tidak di temukan.")
            
    elif pilihan == "5":
        Anggota.lihat_pinjaman()
        
    elif pilihan == "6":
        print("Terima kasih telah menggukan sistem perpustakaan!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
        
if __name__ == "__main__":
    simulasi()
    
        
    
''' bingunggg'''




    
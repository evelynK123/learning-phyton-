'''
Toko online mini 
- produk (harga, nama)
- sorting untuk urutkan harga - termahal 
- urutkan nama produk (A - Z)
control flow function

=> fitur applikasi
- menampilkan menum 
- memilih menu

'''

# data produk -> list -> int, string, dictionary(have key and value), boolean
products = [
    {"nama": "Mouse", "harga": 75000},
    {"nama": "Keyboard", "harga": 150000},
    {"nama": "Flashdisk", "harga": 50000},
    {"nama": "Monitor", "harga": 975000},
    {"nama": "Charger", "harga": 125000},
    {"nama": "cable usb", "harga": 25000},
]

#tampilkan data produk
def tampilkan_produk(produk):
    print("\nDaftar produk: ") 
    for p in produk:
        print(f"- {p['nama']}: Rp{p['harga']}") # untuk cetak nama dan harga

# function sort harga
def selection_sort_byharga(produk): 
    n =  len(produk) #ambil pjg arr/list
    
    #melakukan looping
    
    for i in range(0, n - 1):
        #anggap elemen pertama sebagain nilai yang terkecil
        min_idx = i 
        
        for j in range(i + 1, n ):
            # check apabila nilain list j lebih < [lis min idx]
            if produk[j]['harga'] < produk[min_idx]['harga']:# bisa ganti < atau > tergantung descending ascending 
                min_idx = j 
                produk[i], produk[min_idx] = produk[min_idx], produk[i]
    return produk


def selection_sort_bynama(produk): 
    n =  len(produk) #ambil pjg arr/list
    
    #melakukan looping
    
    for i in range(0, n - 1):
        #anggap elemen pertama sebagain nilai yang terkecil
        min_idx = i 
        
        for j in range(i + 1, n ):
            # check apabila nilain list j lebih < [lis min idx]
            if produk[j]['nama'].lower() < produk[min_idx]['nama'].lower():# bisa ganti < atau > tergantung descending ascending 
                min_idx = j 
                produk[i], produk[min_idx] = produk[min_idx], produk[i]
    return produk


def main():
    #skema app
    print("---Selamat datang di toko online mini---")
    # tampilkan menu dlm looping 
    while True:
        print("\n1. urutkan berdasarkan harga")
        print("2. urutkan berdasarkan nama")
        print("3. tampilkan data produk")
        print("4. keluar/exit")
        
        pilihan = input("pilih menu (1/2/3/4): ")
       # break # berhentiin looping 
        # kondisi 
        if pilihan == "1":
            # urutkan harga produk 
            hasil = selection_sort_byharga(products)
            tampilkan_produk(hasil)
        elif pilihan == "2":
            # urutkan data produk 
            hasil = selection_sort_bynama(products)
            tampilkan_produk(hasil)
        elif pilihan == "3":
            #tampilkan data produk 
            tampilkan_produk(products)
        elif pilihan == "4":
            # tampilkan pesan dampai jumpa 
            print("Terima kasih")
            break 
        else:
            print("pilihan tidak valid, coba lagi!")
    
main()

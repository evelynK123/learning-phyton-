from produk import products
from tampilkan import tampilkan_produk
from sorting import selection_sort_byharga, selection_sort_bynama
from filter import filter_produk_murah

def main():
    #skema app
    print("---Selamat datang di toko online mini---")
    # tampilkan menu dlm looping 
    while True:
        print("\n1. urutkan berdasarkan harga")
        print("2. urutkan berdasarkan nama")
        print("3. tampilkan data produk")
        print("4. tampilkan Produk Murah")
        print("5. keluar/exit")
        
        pilihan = input("pilih menu (1/2/3/4/5): ")
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
            hasil = filter_produk_murah(products)
            tampilkan_produk(hasil)
        elif pilihan == "5":
            # tampilkan pesan dampai jumpa 
            print("Terima kasih")
            break 
        else:
            print("pilihan tidak valid, coba lagi!")
   
#panggil main function         
if __name__ == "__main__":
    main()
    
#make sure safe all files
    

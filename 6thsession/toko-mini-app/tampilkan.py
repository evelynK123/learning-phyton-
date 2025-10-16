#tampilkan data produk
def tampilkan_produk(produk):
    print("\nDaftar produk: ") 
    for p in produk:
        print(f"- {p['nama']}: Rp{p['harga']}") # untuk cetak nama dan harga

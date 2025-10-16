def  filter_produk_murah(produk, batas=100000):
    hasil = [] #list kosong untung menampung produk
    for p in produk:
        if p['harga'] <= batas:
            hasil.append(p)
    return hasil
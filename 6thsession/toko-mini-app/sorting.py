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
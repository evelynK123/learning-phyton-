import tkinter as tk

root = tk.Tk()
root.title("Latihan GUI Pertama")
root.geometry("400x300")
root.mainloop() # apap ini?

import tkinter as tk

root = tk.Tk()
root.title("Mengenal Widget Dasar")

label  = tk.Label(root, taxt= "Masukan Nama: ")
label.pack()

entry = tk.Entry(root)
entry.pack()

def tampilkan_nama():
    nama = entry.get()
    print("Halo,", nama)

button = tk.Button(root, text="Tampilkan Nama", command=tampilkan_nama) #panggil button 
button.pack()

root.mainloop()

# manajemen import
import tkinter as tk 

root = tk.Tk()
root.title("Manajemen Layout")

tk.Label(root, text="Username: ").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="Password:").grid(row=0, column=0)
tk.Entry(root, show="*").grid(row=1, column=1)

tk.Button(root, text="Login").grid(row=2, column=0, columnspan=2)

root.mainloop()

# event handling

import tkinter as tk 
root.title("Event Handling")

def hitungan_luas():
    try:
        sisi = float(entry.get)
        hasil = sisi * sisi
        label_hasil.config(text=f"Luas persegi: {hasil}")
        
    except: 
        label_hasil.config(text="Error: Input harus angka")
        
tk.Label(root, text="Masukkan sisi persegi: ").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Hitung Luas", command=hitungan_luas).pack()


label_hasil = tk.Label(root, text="Hasil akan muncul di sini")
label_hasil.pack()

root.mainloop()


# Error handling dalam GUI
import tkinter as tk
from tkinter import messagebox

root = tk.Tk
root.title("Error handling Dasar")

def bagi_dua():
    try: 
        angka = float(entry.get())
        hasil = angka / 2
        messagebox.showinfo("Hasil",f"Hasil pembagian: {hasil}")
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Tisak bisa dibagi dengan nol!")

tk.Label(root, text="Masukan angka: ").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Bagi Dua", command=bagi_dua).pack()


root.mainloop()

# challenge tambahan

import tkinter as tk 
from tkinter import messagebox

root = tk.Tk
root.title("Konversi Suhu")
root.geometry("400x250")
root.config(bg="#e0f7fa")

judul = tk.Label(root, text="Aplikasi konversi suhu", font=("Arial", 14, "bold"),  bg="#e0f7fa")
judul.pack(pady=10)

tk.Label(root, text="Masukan suhu: ", bg="#e0f7fa").pack()
entry = tk.Entry(root)
entry.pack(pady=5)

pilihan = tk.StringVar(value="Celcius ke Fahrenheit")
opsi = tk.OptionMenu(root, text="Hasil akan muncul di sini",bg="#e0f7fa", font=("Arial", 10))
opsi.pack(pady=10)

def konversi():
    try:
        suhu = float(entry.get())
        if pilihan.get()=="Celcius ke Fahrenheit":
            hasil = (suhu * 9/5) + 32
            label_hasil.config(text=f"{suhu}°C = {hasil:.2f}°F", fg="blue")
        else:
            hasil = (suhu - 32) * 5/9 
            label_hasil.config(text=f"{suhu}°F = {hasil:.2f}°C0", fg="green")
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")
        label_hasil.config(text="Error: Input tidak valid", fg="red")

button = tk.Button(root, text="Konversi", command=konversi, bg="#00796b", fg="white", font=("Arial", 10, "bold"))
button.pack()

def ubah_warna_label(event):
    label_hasil.config(bg="#c8e6c9")
def kembalikan_warna(event):
    label_hasil.config(bg="#e0f7fa")
    

button.bind("<ButtonPress>", ubah_warna_label)
button.bind("<ButtonRelease>", ubah_warna_label)


root.mainloop()
#would anyone buy it, would anyone like it, buat thesis HARUS USEFUL untuk orang2 lain believable lah
# research design 
'''
prof lovaro = crative direction 
cesana = visual design 
nicoletta = more about hard core branding 
cat lady/ giovanna sala= branding more about website app

you can not ask the teacher, write specific misal mau web app yaa tulis kasih kasih hint ttg web
4 or 5 thesis advisor, 
jadi bukan perorangan lebih ke kelas suprevisornya.
'''
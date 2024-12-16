import tkinter as tk
from tkinter import messagebox


def proses_pemesanan():
    film = combo_film.get()
    waktu = combo_waktu.get()
    jumlah_tiket = entry_jumlah.get()

    
    if not film or not waktu or not jumlah_tiket.isdigit() or int(jumlah_tiket) <= 0:
        messagebox.showerror("Kesalahan", "Harap isi semua data dengan benar!")
        return

    jumlah_tiket = int(jumlah_tiket)
    harga_per_tiket = 50000  
    total_harga = jumlah_tiket * harga_per_tiket

    
    ringkasan = f"Film: {film}\nWaktu: {waktu}\nJumlah Tiket: {jumlah_tiket}\nTotal Harga: Rp {total_harga:,}"
    listbox_ringkasan.insert(tk.END, ringkasan)
    listbox_ringkasan.insert(tk.END, "-" * 30)

    
    combo_film.set("")
    combo_waktu.set("")
    entry_jumlah.delete(0, tk.END)


def keluar():
    root.destroy()


root = tk.Tk()
root.title("Sistem Pemesanan Tiket Bioskop")


label_judul = tk.Label(root, text="Pemesanan Tiket Bioskop", font=("Arial", 16))
label_judul.pack(pady=10)


label_film = tk.Label(root, text="Pilih Film:")
label_film.pack()
combo_film = tk.StringVar()
dropdown_film = tk.OptionMenu(root, combo_film, "Avengers: Endgame", "Spider-Man: No Way Home", "The Batman", "Frozen 2")
dropdown_film.pack()


label_waktu = tk.Label(root, text="Pilih Waktu Tayang:")
label_waktu.pack()
combo_waktu = tk.StringVar()
dropdown_waktu = tk.OptionMenu(root, combo_waktu, "10:00", "13:00", "16:00", "19:00", "21:00")
dropdown_waktu.pack()


label_jumlah = tk.Label(root, text="Jumlah Tiket:")
label_jumlah.pack()
entry_jumlah = tk.Entry(root)
entry_jumlah.pack()


btn_pesan = tk.Button(root, text="Pesan Tiket", command=proses_pemesanan)
btn_pesan.pack(pady=5)


label_ringkasan = tk.Label(root, text="Ringkasan Pemesanan:")
label_ringkasan.pack()
listbox_ringkasan = tk.Listbox(root, width=50, height=10)
listbox_ringkasan.pack()


btn_keluar = tk.Button(root, text="Keluar", command=keluar)
btn_keluar.pack(pady=5)

root.mainloop()
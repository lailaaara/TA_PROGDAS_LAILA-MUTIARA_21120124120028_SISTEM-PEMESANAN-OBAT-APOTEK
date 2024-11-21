import tkinter as tk
from tkinter import messagebox, StringVar, ttk

class Apotek:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistem Pemesanan Obat Apotek")
        self.master.geometry("400x400")
        self.master.configure(bg="lavenderblush")

        self.data_pembeli = ()
        self.data_pembeli_frame = None  
        self.home_frame = None
        self.pemesanan_frame = None

        self.create_data_pembeli_frame()

    def show_frame(self, frame):
     for widget in self.master.winfo_children():
        widget.pack_forget()  
     frame.pack(padx=20, pady=20)

    def create_data_pembeli_frame(self):
        if self.data_pembeli_frame:
            self.data_pembeli_frame.destroy()  
        
        self.data_pembeli_frame = tk.Frame(self.master, bg="lavenderblush")
        self.data_pembeli_frame.pack(padx=20, pady=20)

        tk.Label(self.data_pembeli_frame, text="Data Pembeli", font=("Arial", 14), bg="lavenderblush").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.data_pembeli_frame, text="Nama :", font=("Times new roman", 13), bg="lavenderblush").grid(row=1, column=0, sticky="w")
        self.entry_nama = tk.Entry(self.data_pembeli_frame)
        self.entry_nama.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.data_pembeli_frame, text="Usia :", font=("Times new roman", 13), bg="lavenderblush").grid(row=2, column=0, sticky="w")
        self.entry_usia = tk.Entry(self.data_pembeli_frame)
        self.entry_usia.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.data_pembeli_frame, text="Selanjutnya", command=self.submit_data_pembeli, bg="ghostwhite", fg="black").grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.data_pembeli_frame, text="Exit", command=self.exit_app, bg="ghostwhite", fg="black").grid(row=4, columnspan=2, pady=10)

    def submit_data_pembeli(self):
        nama = self.entry_nama.get()
        usia = self.entry_usia.get()

        if not nama or not usia:
            messagebox.showerror("Error", "Silahkan isi semua data pembeli.")
            return 

        if not nama.isalpha():
            messagebox.showerror("Error", "Nama hanya boleh terdiri dari huruf.")
            return

        if not usia.isdigit():
            messagebox.showerror("Error", "Usia harus berupa angka.")
            return

        if self.validasi_input(nama, usia):
            self.data_pembeli = {'nama': nama, 'usia': usia}
            messagebox.showinfo("Data Pembeli", f"Nama: {nama}\nUsia: {usia}")

            self.create_home_frame()
            self.show_frame(self.home_frame)

    def validasi_input(self, nama, usia):
        usia = int(usia)
        if usia < 1 or usia > 150:
            messagebox.showerror("Error", "Usia harus antara 1 dan 150.")
            return False
        return True


    def create_home_frame(self):
        if self.home_frame:
            self.home_frame.destroy() 
        self.home_frame = tk.Frame(self.master, bg="lavenderblush")
        self.home_frame.pack(padx=20, pady=20)

        tk.Label(self.home_frame, text="Selamat Datang di Apotek Bahagia", bg="lavenderblush", font=("Arial", 16)).grid(row=0, columnspan=2, pady=10)

        tk.Label(self.home_frame, text="Keluhan Penyakit:", font=("Times new roman", 13), bg="lavenderblush").grid(row=1, column=0, pady=5)
        self.keluhan_entry = tk.Entry(self.home_frame)
        self.keluhan_entry.grid(row=1, column=1, pady=5)

        tk.Button(self.home_frame, text="Rekomendasi Obat", command=self.rekomendasi_obat, bg="ghostwhite", fg="black").grid(row=2, columnspan=2, pady=10)

        self.label_rekomendasi = tk.Label(self.home_frame, text="", bg="lavenderblush", wraplength=300)
        self.label_rekomendasi.grid(row=3, columnspan=2, pady=10)

        tk.Button(self.home_frame, text="Pemesanan Obat", command=self.create_pemesanan_frame, bg="ghostwhite", fg="black").grid(row=4, columnspan=2, pady=10)
        tk.Button(self.home_frame, text="Back", command=lambda: self.show_frame(self.data_pembeli_frame), bg="ghostwhite", fg="black").grid(row=5, columnspan=2, pady=10)
        
        self.show_frame(self.home_frame)

    def rekomendasi_obat(self):
        keluhan = self.keluhan_entry.get().lower()
        rekomendasi = ""

        if "sakit kepala" in keluhan:
            rekomendasi = "Rekomendasi: Paracetamol, Ibuprofen"
        elif "flu" in keluhan:
            rekomendasi = "Rekomendasi: Paracetamol, Cetirizine"
        elif "infeksi" in keluhan:
            rekomendasi = "Rekomendasi: Amoxicillin"
        elif "diare" in keluhan:
            rekomendasi = "Rekomendasi: Loperamide"
        elif "batuk" in keluhan:
            rekomendasi = "Rekomendasi: Cetirizine"
        else:
            rekomendasi = "Rekomendasi: Silakan konsultasikan lebih lanjut."

        self.label_rekomendasi.config(text=rekomendasi)

    def create_pemesanan_frame(self):
        self.home_frame.pack_forget()
        self.pemesanan_frame = tk.Frame(self.master, bg="lavenderblush")
        self.pemesanan_frame.pack(padx=20, pady=20)

        tk.Label(self.pemesanan_frame, text="Pilih Obat:", font=("Times new roman", 13), bg="lavender").grid(row=0, column=0, pady=5)

        self.produk = {
            'Paracetamol': {'harga': 5000, 'jumlah': 50},
            'Ibuprofen': {'harga': 7000, 'jumlah': 50},
            'Amoxicillin': {'harga': 15000, 'jumlah': 50},
            'Cetirizine': {'harga': 6000, 'jumlah': 50},
            'Loperamide': {'harga': 8000, 'jumlah': 50},
        }

        self.selected_obat = StringVar()
        self.dropdown_obat = ttk.Combobox(self.pemesanan_frame, textvariable=self.selected_obat)
        self.dropdown_obat['values'] = list(self.produk.keys())
        self.dropdown_obat.grid(row=1, column=1, pady=5)

        tk.Label(self.pemesanan_frame, text="Jumlah:", font=("Times new roman", 13), bg="lavender").grid(row=2, column=0, pady=5)
        self.entry_jumlah = tk.Entry(self.pemesanan_frame)
        self.entry_jumlah.grid(row=2, column=1, pady=5)

        tk.Button(self.pemesanan_frame, text="Tambah ke Keranjang", command=self.tambah_ke_keranjang, bg="pink", fg="black").grid(row=3, columnspan=2, pady=10)

        tk.Button(self.pemesanan_frame, text="Hitung Total", command=self.hitung_total, bg="pink", fg="black").grid(row=4, columnspan=2, pady=10)

        self.label_total = tk.Label(self.pemesanan_frame, text="Total: Rp 0", bg="#f0f0f0")
        self.label_total.grid(row=5, columnspan=2, pady=10)

        tk.Button(self.pemesanan_frame, text="Kembali ke Home", command=self.kembali_ke_home, bg="pink", fg="black").grid(row=6, columnspan=2, pady=10)

        self.cart = {}

    def tambah_ke_keranjang(self):
        obat = self.selected_obat.get()
        try:
            jumlah = int(self.entry_jumlah.get())
            if obat in self.produk:
                if self.produk[obat]['jumlah'] >= jumlah:
                    if obat in self.cart:
                        self.cart[obat] += jumlah
                    else:
                        self.cart[obat] = jumlah
                    self.produk[obat]['jumlah'] -= jumlah
                    messagebox.showinfo("Info", f"'{obat}' berhasil ditambahkan ke keranjang.")
                    self.entry_jumlah.delete(0, tk.END)  
                else:
                    messagebox.showerror("Error", f"Stok '{obat}' tidak cukup.")
            else:
                messagebox.showerror("Error", "Obat tidak ditemukan.")
        except ValueError:
            messagebox.showerror("Error", "Masukkan jumlah yang valid.")

    def hitung_total(self):
        total = sum(self.produk[obat]['harga'] * jumlah for obat, jumlah in self.cart.items())
        self.label_total.config(text=f"Total: Rp {total}")
        self.create_konfirmasi_frame(total)

    def create_konfirmasi_frame(self, total):
        self.pemesanan_frame.pack_forget()
        self.konfirmasi_frame = tk.Frame(self.master, bg="lavenderblush")
        self.konfirmasi_frame.pack(padx=20, pady=20)

        tk.Label(self.konfirmasi_frame, text="Konfirmasi Pemesanan", bg="lavenderblush", font=("Arial", 16)).grid(row=0, columnspan=2, pady=10)

        tk.Label(self.konfirmasi_frame, text=f"Nama: {self.data_pembeli['nama']}", bg="lavenderblush").grid(row=2, columnspan=2, sticky='w', pady=5)
        tk.Label(self.konfirmasi_frame, text=f"Usia: {self.data_pembeli['usia']}", bg="lavenderblush").grid(row=3, columnspan=2, sticky='w', pady=5)

        row = 4
        for obat, jumlah in self.cart.items():
            tk.Label(self.konfirmasi_frame, text=f"{obat} x {jumlah}", bg="lavenderblush").grid(row=row, column=0, sticky='w', pady=5)
            tk.Label(self.konfirmasi_frame, text=f"Rp {self.produk[obat]['harga'] * jumlah}", bg="lavenderblush").grid(row=row, column=1, sticky='e', pady=5)
            row += 1

        tk.Label(self.konfirmasi_frame, text="Total yang harus dibayar:", bg="lavenderblush", font=("Arial", 14)).grid(row=row, column=0, sticky='w', pady=10)
        tk.Label(self.konfirmasi_frame, text=f"Rp {total}", bg="lavenderblush", font=("Arial", 14)).grid(row=row, column=1, sticky='e', pady=10)

        tk.Button(self.konfirmasi_frame, text="Konfirmasi Pembayaran", command=self.konfirmasi_pembayaran, bg="pink", fg="black").grid(row=row+1, columnspan=2, pady=10)
        tk.Button(self.konfirmasi_frame, text="Kembali ke Pemesanan", command=self.kembali_ke_pemesanan, bg="pink", fg="black").grid(row=row+2, columnspan=2, pady=10)

        # Menambahkan tombol kembali ke home
        tk.Button(self.konfirmasi_frame, text="Kembali ke Home", command=self.kembali_ke_home, bg="pink", fg="black").grid(row=row+3, columnspan=2, pady=10)


    def konfirmasi_pembayaran(self):
        messagebox.showinfo("Info", "Pembayaran berhasil! Terima kasih atas pesanan Anda.")
        self.reset_aplikasi()

    def kembali_ke_pemesanan(self):
        self.konfirmasi_frame.pack_forget()
        self.create_pemesanan_frame()

    def kembali_ke_home(self):
        self.pemesanan_frame.pack_forget()
        self.create_home_frame()

    def reset_aplikasi(self):
        self.cart.clear()
        self.data_pembeli = {'nama': '', 'usia': 0}  
        self.create_data_pembeli_frame() 
        self.show_frame(self.data_pembeli_frame)

    def exit_app(self):
        if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Apotek(root)
    root.mainloop()
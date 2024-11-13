import tkinter as tki  # impor modul tkinter sebagai 'tki' untuk membuat GUI.

# Fungsi untuk menampilkan hasil prediksi
def prediksi_prodi():
    # Mengubah teks di "hasil_label" untuk menampilkan prediksi program studi yang dipilih.
    hasil_label.config(text="Prodi Pilihan: Teknologi Informasi")

# Membuat jendela utama
root = tki.Tk()  
root.title("Aplikasi Prediksi Prodi Pilihan")  # Mengatur judul dari jendela utama.
root.geometry("600x800")  # Mengatur ukuran jendela utama menjadi 600x800 piksel.

# Label judul
judul_label = tki.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Times New Roman", 16))  
# Membuat label judul di jendela utama dengan teks dan font yang ditentukan.
judul_label.pack(pady=10)  # Menempatkan label judul di jendela dengan jarak vertikal (padding) 10 piksel.

# Membuat input untuk nilai mata pelajaran
for i in range(1, 11):  # Loop untuk membuat input bagi nilai 10 mata pelajaran.
    # Membuat label untuk setiap mata pelajaran dengan nomor yang sesuai.
    label = tki.Label(root, text=f"Nilai Mata Pelajaran {i}:", font=("Times New Roman", 12))
    label.pack(anchor="w", padx=20)  # Menempatkan label dengan perataan ke kiri dan padding horizontal 20 piksel.

    # Membuat input untuk memasukkan nilai mata pelajaran.
    entry = tki.Entry(root, font=("Arial", 12))
    entry.pack(pady=5, padx=20, fill="x") 

# Button untuk mendapatkan hasil prediksi
prediksi_button = tki.Button(root, text="Hasil Prediksi", command=prediksi_prodi, font=("Times New Roman", 12))  
# Membuat tombol untuk memanggil fungsi prediksi_prodi ketika ditekan.
prediksi_button.pack(pady=20)  # Menempatkan tombol dengan jarak vertikal (padding) 20 piksel.

# Label untuk menampilkan hasil prediksi
hasil_label = tki.Label(root, text="", font=("Times New Roman", 14), fg="black")  
# Membuat label kosong yang akan menampilkan hasil prediksi setelah tombol ditekan.
hasil_label.pack(pady=10)  # Menempatkan label hasil dengan jarak vertikal 10 piksel.


root.mainloop()  # Memulai event loop dari tkinter agar jendela tetap terbuka sampai ditutup oleh pengguna.



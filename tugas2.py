# Menyimpan 5 nama produk dalam array
produk = ["mie ayam", "nasi goreng", "ayam", "sego pecel", "es teh anget"]

# Menampilkan semua nama produk ke layar
print("Daftar Produk:")
for i, nama in enumerate(produk, start=1):
    print(f"{i}. {nama}")

# Meminta pengguna memasukkan nomor urut produk
nomor = int(input("Masukkan nomor produk yang ingin dilihat (1-5): "))

# Validasi agar tidak terjadi IndexError
if 1 <= nomor <= len(produk):
    print(f"Produk nomor {nomor}: {produk[nomor-1]}")
else:
    print("Nomor produk tidak valid!")

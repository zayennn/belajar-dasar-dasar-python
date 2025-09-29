# input user

data = input("Masukkan data: ")

print("Data yang dimasukkan:", data, type(data))


# ubah data dari user menggunakan casting

data_int = int(input("Masukkan angka: ")) # casting ke int
print("Data yang dimasukkan:", data_int, type(data_int))

data_bool = bool(int(input("Masukkan angka: "))) # casting ke bool
print("Data yang dimasukkan:", data_bool, type(data_bool))
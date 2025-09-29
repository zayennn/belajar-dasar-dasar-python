# latihan konversi satuan temperature

print("\nProgram Konversi Satuan Temperature\n")

# input suhu dalam celcius
celcius = float(input("Masukkan suhu dalam celcius: "))
print("Suhu adalah", celcius, "Celsius")

# reamur
reamur = (4/5) * celcius
print("Suhu dalam Reamur adalah", reamur, "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah", kelvin, "Kelvin")
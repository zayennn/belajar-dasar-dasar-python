# operasi logika atau boolean
# not, or, and, xor


# NOT ( kebalikan )
print("==== NOT ====")

a = True
b = not a

print('data a =', a)
print('============NOT')
print('data b =', b)



# OR ( jika salah satu True, maka hasilnya True )
print("\n==== OR ====")
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)



# AND ( jika kedua-duanya True, maka hasilnya True )
print("\n==== AND ====")
a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)



# XOR ( jika salah satu True, maka hasilnya True, jika kedua-duanya sama-sama True atau False, maka hasilnya False/True  )
print("\n==== XOR ====")
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
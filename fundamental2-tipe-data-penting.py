print('tipe data skalar => tipe data sederhana')
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catir'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list/daftar/array')
anak = ['Eko', 'Dwi', 'Tri', 'Catir']
print(anak)
anak.append('saddam')
print(anak)

print('\nsapa anak ke-2')
print('Hello %s :)' % anak[1])
print('Hello', anak[1], ':)')
print(f'Hello {anak[1]} :)')

print('\nsapa semua anak')
for j in anak :
    print(f'Hello {j} :D')

print('\nsapa semua anak menggunakan for in range / cara ribet')
for j in range(len(anak)) :
    print(f'{j + 1}. Hello {anak[j]} :0')

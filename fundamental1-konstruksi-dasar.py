# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL: Eksekusi berurutan
print('Hello World!')
print('by SADDAM')
print('Tanggal 15 Juni 2020')
print('-' * 10)

# PERCABANGAN: Ekeskusi terpilih
ingin_cepat = True

if ingin_cepat:
    print('Lewat jalan lurus aja ya!')
else:
    print('Lewat jalan lain')

# PERULANGAN
print('Menggunakan while:')
jumlah_anak = 4
i = 1

while i <= jumlah_anak:
    print('Hello anak ke -', i)
    i += 1

print('Menggunakan for:')
for i in range(1, jumlah_anak + 1):
    # print('Hello anak ke - %s' % i)
    # print('Hello anak ke -', i)
    print(f'Hello anak ke - {i}')



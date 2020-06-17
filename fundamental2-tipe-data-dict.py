'''
Tipe data dictionary sejedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
'''

kamus_ind_eng = {
    'anak' : 'son',
    'istri' : 'wife',
    'ayah' : 'father',
    'ibu' : 'mother'
}

print(kamus_ind_eng)
print(type(kamus_ind_eng))

kamus_ind_eng = {}
kamus_ind_eng['anak'] = 'son'
kamus_ind_eng['istri'] = 'wife'
kamus_ind_eng['ayah'] = 'father'
kamus_ind_eng['ibu'] = 'mother'

print(kamus_ind_eng)
print(type(kamus_ind_eng))
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])
# print(kamus['mother']) # kebalikan tidak bisa / hanya berlaku satu arah

print('\nData ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal' : '2020-06-10',
    'driver_list' : [
        {'nama' : 'Eko', 'jarak' : 10},
        {'nama' : 'Dwi', 'jarak' : 30},
        {'nama' : 'Tri', 'jarak' : 40},
        {'nama' : 'Catir', 'jarak' : 1000}
    ]
} # dict > list > dict

print(data_dari_server_gojek)
print(f"\nDriver disekitar sini: {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")

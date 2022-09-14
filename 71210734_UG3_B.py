#UG Strukdat_3
randata = int(input("Masukkan range data:"))

def fakt(n):
   if n == 0 or n == 1:
       return n
   else:
       return n*fakt(n-1)

li = []
for i in range (0,randata):
    if i % 2 == 0:
        li.append(i)
    else:
        continue

faakt =[]
for j in li:
    if j % 2 == 0:
        mam = fakt(j)
        faakt.append(mam)
    else:
        continue

dikt = dict(zip(li, faakt))

print(dikt)

cari = int(input("Data Ditampilkan:"))
if cari in dikt:
    print('Data ditemukan')
    print('Data yang ditemukan bernilai:',dikt.get(cari))
else:
    print('Data tidak ditemukan')

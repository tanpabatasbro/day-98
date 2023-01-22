print("TIKET PESAWAT JAKARTA - TOKYO (PULANG PERGI)")

tiket = {
    "Garuda Indonesia" : 13_750_000,
    "Air Asia Indonesia" : 10_060_000 
}
print(60*"=")
print("DAFTAR TIKET PESAWAT")
print(60*"=")

for i in tiket:
    print(f"tiket pesawat : {i}\tHarga : {tiket[i]}")
    
print("PEMBELIAN LEBIH DARI 3 DISKON 10%")
print(60*"=")

nama = input("Nama Pemesan : ")
beli = input("Pilih Tiket  :  ")
jumlah = int(input("Jumlah Tiket : "))
bayar = jumlah * tiket[beli]

if jumlah > 3 :
    diskon = 10/100
    total_bayar = bayar * diskon
    
else: 
    total_bayar = bayar
    
print(f"\nNama Pemesan : {nama}")
print(f"Tiket Pesawat : {beli}")
print(f"Jumlah : {jumlah}")
print(f"Harga Total : Rp.{total_bayar}")
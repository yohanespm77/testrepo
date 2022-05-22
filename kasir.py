import time

pembeli = input("Masukkan nama pembeli : ")
pilihan = """
Selamat datang di Kios BXBY
------------------------------
Daftar Harga
1. | Susu          |= Rp8.000
2. | Minyak telon  |= Rp41.000
3. | Lotion        |= Rp30.000
4. | Baby oil      |= Rp12.000
5. | Parfum        |= Rp70.000
6. | Shampoo       |= Rp15.000
7. | Sabun         |= Rp7.000
8. | Glade         |= Rp30.000
------------------------------
""" 
data = {}
def daftar():
    print(pilihan)
    pesan = input("Mau beli apa kak ? : ")
    item = ["susu","minyak telon","lotion","baby oil","parfum","shampoo","sabun","glade"]
    if pesan not in item:
        print("Maaf, barang tidak tersedia :(\n")
    else:
        jumlahpesan = int(input("Mau beli berapa ? : "))
        if pesan.lower() == "susu":
            harga = (8000*jumlahpesan)
            if pesan.lower() not in data:
                data[pesan.lower()] = jumlahpesan
            else:
                data[pesan.lower()] += jumlahpesan       
        elif pesan.lower() == "minyak telon":
            harga = (41000*jumlahpesan)
            if pesan.lower() not in data:
                data[pesan.lower()] = jumlahpesan
            else:
                data[pesan.lower()] += jumlahpesan
        elif pesan.lower() == "lotion":
            harga = (30000*jumlahpesan)
            if pesan.lower() not in data:
                data[pesan.lower()] = jumlahpesan
            else:
                data[pesan.lower()] += jumlahpesan
        elif pesan.lower() == "baby oil":
            harga = (12000*jumlahpesan)
            if pesan.lower() not in data:
                data[pesan.lower()] = jumlahpesan
            else:
                data[pesan.lower()] += jumlahpesan
        elif pesan.lower() == "parfum":
            harga = (70000*jumlahpesan)
            if pesan.lower() not in data:
                data[pesan.lower()] = jumlahpesan
            else:
                data[pesan.lower()] += jumlahpesan
        elif pesan.lower() == "shampoo":
            harga = (15000*jumlahpesan)
            if pesan.lower() not in data:
                data[pesan.lower()] = jumlahpesan
            else:
                data[pesan.lower()] += jumlahpesan
        elif pesan.lower() == "sabun":
            harga = (7000*jumlahpesan)
            if pesan.lower() not in data:
                data[pesan.lower()] = jumlahpesan
            else:
                data[pesan.lower()] += jumlahpesan
        elif pesan.lower() == "glade":
            harga = (30000*jumlahpesan)
            if pesan.lower() not in data:
                data[pesan.lower()] = jumlahpesan
            else:
                data[pesan.lower()] += jumlahpesan
menu = "yes"
while menu == "yes":
    daftar()
    client = input("Apakah ingin tambah pembelian ? Y/N : ")   
    if client.lower() == "n":
        menu = "stop"

price = 0
for i in data:
    if i == "susu":
        price += 8000*data[i]
    elif i == "minyak telon":
        price += 41000*data[i]
    elif i == "lotion":
        price += 30000*data[i]
    elif i == "baby oil":
        price += 12000*data[i]
    elif i == "parfum":
        price += 70000*data[i]
    elif i == "shampoo":
        price += 15000*data[i]
    elif i == "sabun":
        price += 7000*data[i] 
    elif i == "glade":
        price += 30000*data[i]      

print("Total Harga ",price)
if price != 0:
    uang = int(input("uangnya berapa ya kak ? : Rp"))
    if price > uang:
        print("Maaf, uang kakak tidak cukup :(")
    else:    
        kembalian = int(uang-price)
        print("\n\n=========================")
        print("====== BXBY'S KIOS ======")
        print("=========================")
        localtime = time.asctime(time.localtime(time.time()))
        print(localtime,"\n")
        print("Nama Pembeli : "+str(pembeli))
        print("Barang yang dibeli :")
        no=0
        for x in data:
            no+=1
            print(f"{no}. {x} ({data[x]})")
        jumbar=0
        for y in data:
            jumbar += data[y]
        print("Total Pesanan : "+str(jumbar)+" pcs")
        print("----------------------")
        print("Total     : Rp"+str(price))     
        print("Cash      : Rp"+str(uang)) 
        print("Kembalian : Rp"+str(kembalian)+"\n")
else:
    print("Anda tidak membeli apa-apa")
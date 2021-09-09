import carList

def main():
    
    print("Program Daftar Mobil")
    print("xxxxxxxxxxxxxxxxxxxx")
    print()
    userName = input("Nama Anda: ")
    print()
    print()

    namaMobil = input("Nama Mobil: ")
    print()
    
    merekMobil = input("Merek Mobil: ")
    print()
    tahunMobil = input("Tahun: ")
    print()
    hargaMobil = int(input("Harga: "))
    print()

    finalMobil = carList.car(namaMobil, merekMobil, tahunMobil, hargaMobil )
    print()

    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print(f"Output Yang diinput oleh: \n{userName}\n")
    print(f"{namaMobil} dengan merek berupa {merekMobil} tahun {tahunMobil}.\nHarganya mulai dari {hargaMobil}  ")


main()


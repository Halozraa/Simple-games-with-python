#ini adalah game tebak tebakan posisi

import random

def start():
    #eksekusi
    while True:
        # Mendapatkan posisi penjahat
        person_position = random.randint(1, 6)

        # Bentuk goa kosong
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 6
        goa = goa_kosong.copy()
        goa[person_position - 1] = "|0_0|"
        goa = " ".join(goa)  # Menggabungkan elemen dalam list goa menjadi satu string

        # Input user (User disuruh memilih)
        while True:
            print("\nAda penjahat nih bersembunyi diantara goa ini\n")
            print(" ".join(goa_kosong))  # Menampilkan bentuk goa kosong
            pilihan = int(input("Ada dinomer berapa penjahatnya [1/2/3/4/5/6]: "))
            if pilihan in [1, 2, 3, 4, 5, 6]:
                break
            else:
                print("## Coba Masukan Jawaban yang Ada dipilihan itu ##")

    # PENENTU KEMENANGAN ATAU KEKALAHAN
        if pilihan == person_position:
            print("\nPenjahatnya ada disini ⬇️")
            print(f"\n{goa}\n### Selamat kamu Menang 🏆 ###\n")
        else:
            print("\nPenjahatnya ada disini ⬇️")
            print(f"\n{goa}\n### Kamu Kalah idiot ###\n")
    
    # MEMASTIKAN MASIH MAU BERMAIN ATAU TIDAK
        play_again = input("Mau tetap main [y/n]: ")
        if play_again.lower() == "n":
            break
if __name__ == '__main__':
    start()

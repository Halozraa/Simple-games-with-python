#ini adalah game math

import random
def start():
    def operasi_bilangan(x, y, operator):
        if operator == 'perkalian':
            return x * y
        elif operator == 'pembagian':
            return x / y
        elif operator == 'pertambahan':
            return x + y
        elif operator == 'pengurangan':
            return x - y
        else:
            return "Operator tidak valid"

    while True:
        # Data penampung
        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 10)

        # Memilih operasi
        print(f"Dibawah ini ada Tes soal Matematika\n 1. pertambahan\n 2. pengurangan\n 3. perkalian\n 4. Pembagian")

        # Input dari user
        memilih = input("Mau Test yang mana: ")

        # Memilih operasi
        if memilih == "1":
            operator = 'pertambahan'
        elif memilih == "2":
            operator = 'pengurangan'
        elif memilih == "3":
            operator = 'perkalian'
        elif memilih == "4":
            operator = 'pembagian'
        else:
            print("Masukan dengan benar  di list pilihan yang ada !")
            continue

        # Menghitung hasil operasi
        hasil = operasi_bilangan(angka1, angka2, operator)

        # Menampilkan soal
        print(f"Soalnya adalah {angka1} {'+' if operator == 'pertambahan' else '-' if operator == 'pengurangan' else '*' if operator == 'perkalian' else '/'} {angka2}")

        # Jawaban user
        jawab_user = input("Jawabannya adalah: ")

        # Mengonversi jawaban user menjadi tipe data float
        try:
            jawab_user = float(jawab_user)
        except ValueError:
            print("Masukkan jawaban berupa angka!")
            continue

        # Memeriksa jawaban user
        if jawab_user == hasil:
            print("Jawaban kamu benar")
        else:
            print(f"Jawaban kamu salah, Hasilnya adalah {hasil}")

    # MEMASTIKAN MASIH MAU BERMAIN ATAU TIDAK
        play_again = input("Mau tetap main [y/n]: ")
        if play_again.lower() == "n":
            break
if __name__ == '__main__':
    start()

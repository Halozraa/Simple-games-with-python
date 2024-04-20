from libs import welcome_message, end_program
from libs import print_red
from games import games1, games2
import socket



def menu():
    while True:
        try:
            pilihan = int(input("\nPilihan Program\n 1. Tebak-Tebakan\n 2. Math games\n 3. Mini Mart\n 4. keluar \n Mau apa : "))
            if pilihan == 1:
                games1.start()
            elif pilihan == 2:
                games2.start()
            elif pilihan == 3:
                print_red(f"\nMaafkan Hamba ini fitur ini belum tersedia {socket.gethostname()}")
           
            elif pilihan == 4:
                end_program()
            else:
                print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
        except ValueError:
            print("Masukkan angka yang valid.")

def main():
    welcome_message()
    menu()

if __name__ == '__main__':
    main()

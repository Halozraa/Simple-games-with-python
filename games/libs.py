import socket
from time import sleep

def welcome_message():
    nama_pc = socket.gethostname()
    dekor = "*" * (len(nama_pc)+6)
    print(dekor)
    print(f"** {nama_pc} **")
    print(dekor)
    

def end_program ():
    sleep(1)
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print("1...")
    sleep(1)
    print("0...")
    print("Program telah berakhir")
    exit()

def print_red(text):
    red_color = "\033[91m"
    reset_color = "\033[0m"
    print(red_color + text + reset_color)
        
def print_green(text):
    green_color = "\033[92m"
    reset_color = "\033[0m"
    print(green_color + text + reset_color)

def print_yellow(text):
    yellow_color = "\033[93m"
    reset_color = "\033[0m"
    print(yellow_color + text + reset_color)

if __name__ == '__main__':
    welcome_message()
    end_program()
    print_red()

    

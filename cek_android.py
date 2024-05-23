import os
import time

def clear_screen():
    os.system('clear')  # Menghapus layar terminal

def print_ky_logo():
    logo = """ 
    
    
     ⠀⠀⠀⢀⣠⡄⠀⠀⣴⣶⣶⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣾⣿⡿⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣿⣿⣿⠁⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣿⠏⠀⠀⠾⠿⠿⣿⣿⣿⡿⠿⠿⠿⠿⠿⢿⣷⡀⠀
⠀⣾⣿⣿⣿⣿⡏⠀⠀⣤⣤⠀⠀⢸⣿⡿⠀⠀⢠⣤⡄⠀⠀⣿⣷⠀
⢠⣿⣿⣿⣿⡿⠁⠀⢰⣿⠏⠀⢀⣾⣿⠃⠀⢀⣿⡿⠁⠀⣰⣿⣿⡄
⢸⣿⣿⣿⣿⠃⠀⢀⣿⡿⠀⠀⣸⣿⠇⠀⠀⣾⣿⠃⠀⢰⣿⣿⣿⡇
⠘⣿⣿⣿⠇⠀⠀⣾⣿⠁⠀⢰⣿⡟⠀⠀⣰⣿⠇⠀⢀⣾⣿⣿⣿⠃
⠀⢿⣿⡟⠀⠀⣸⣿⠃⠀⢠⣿⡿⠁⠀⠀⠛⠛⠀⠀⣼⣿⣿⣿⡿⠀
⠀⠈⢿⣶⣶⣶⣿⣿⣶⣶⣾⣿⠇⠀⢠⣶⣶⣶⣶⣾⣿⣿⣿⡿⠁⠀
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀
⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⡿⠀⠀⣸⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠁⠀⠰⠿⠿⠛⠛⠋⠁⠀⠀⠀⠀
       author devil 
================================
"""
    print(logo)

def run_command(command):
    result = os.popen(command).read()
    return result.strip()

def main():
    clear_screen()
    print_ky_logo()
    
    print("Konfigurasi jaringan:")
    print(run_command("ifconfig"))
    time.sleep(2)  # Memberikan jeda 2 detik

    print("\nMerek HP Anda:")
    brand = run_command("getprop ro.product.brand")
    model = run_command("getprop ro.product.model")
    print(f"Brand: {brand}")
    print(f"Model: {model}")

    # Mendapatkan informasi RAM
    mem_total = int(run_command("grep MemTotal /proc/meminfo | awk '{print $2}'"))
    mem_available = int(run_command("grep MemAvailable /proc/meminfo | awk '{print $2}'"))

    # Mengkonversi dari KB ke MB
    mem_total_mb = mem_total // 1024
    mem_available_mb = mem_available // 1024

    print(f"\nTotal Memori: {mem_total_mb} MB")
    print(f"Memori Tersedia: {mem_available_mb} MB")

if __name__ == "__main__":
    main()
import base64
import random
import string

# Algoritma Pseudo Random Number Generator
def random_character_generator(size):
    characters = string.ascii_uppercase + string.digits
    random_str = ''.join(random.choice(characters) for _ in range(size))
    return random_str

# Encoding Base 64
def base64_encode(data):
    base64_bytes = base64.b64encode(data.encode('utf-8'))
    base64_text = str(base64_bytes, 'utf-8')
    return base64_text

# Pemotongan Text
def cut_text(text, length):
    return text[:length]

# Fungsi Captcha
def generate_captcha():
    random_characters = random_character_generator(5)  # 5 karakter acak
    base64_string = base64_encode(random_characters)  # mengenkode karakter dengan base64
    captcha = cut_text(base64_string, 10)  # memotong 10 karakter dari kiri
    return captcha

# Fungsi Verifikasi Captcha
def verify_captcha(user_input, captcha):
    return user_input == captcha

# Program Captcha untuk Pengamanan Login
if __name__ == "__main__":
    # Membuat dan menampilkan Captcha
    captcha = generate_captcha()
    print("Selamat datang! Silakan login.")
    print("Captcha Anda adalah:", captcha)
    
    # Meminta input dari pengguna
    user_input = input("Silahkan Masukkan Captcha Anda: ")
    
    # Verifikasi input pengguna
    if verify_captcha(user_input, captcha):
        print("Captcha anda benar! Akses diberikan kepada anda!")
        # Tambahan: Tempatkan logika login Anda di sini
    else:
        print("Captcha salah! Akses ditolak anda harus masukkan ulang!")

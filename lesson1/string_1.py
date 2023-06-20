import os
from time import sleep

# clear layar terlebih dahulu
os.system("clear")

# tampilkan judul aplikasi
title = """
============================
A P L I K A S I - M U M Z Z 
============================
"""

print(title)

sleep(3)

username = input("masukan username : ")
address = input("masukan alamat : ")
phone = input("masukan phone : ")
email = input("masukan email : ")

text = f"""

------------------------------------------
    nama        : { username }
------------------------------------------
    alamat      : { address }
------------------------------------------
    phone       : { phone }
------------------------------------------
    email       : { email }
------------------------------------------
"""
os.system("clear")

sleep(3)

print(text)
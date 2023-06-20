def cekUsia(usia):
    if usia < 20 :
        print("kamu belum bisa masuk")
    else:
        print("silahkan masuk")


def checkUsername():
    username = input("masukan username : ")

    if username == "mumzz":
        print("login berhasil")
    else :
        print("username tidak terdaftar")


def login():
    username = input("masukan username : ")
    password = input("masukan password : ")
    if username == "mumzzuyee" and password == "123":
        print("yeayy login berhasil!!")
    else :
        print("login gagal coeg -,-")


def login2():
    username = input("masukan username : ")
    password = input("masukan password : ")

    if username != "mumzz" != "123":
        print("Username salah brooo")
        return
    
    if username !=password != "123":
        print("password salah brooo")
        return
    
    print("Welcome Broooo !!!")

def login3():
    dataUsername = ["mumzz", "mamzz", "mimzz"]
    dataPassword = ["123", "234", "321"]

    username = input("masukin usernamenya broo : ")

    if username not in dataUsername:
        print("Username salah brooo!! : ")
        return
    
    password = input("masukin passwordnya broo")

    if password not in dataPassword:
        print("inget-inget lagi passwordnya broo")
        return
    
    print("""Nahhh Sekarang Lu Udah Berhasil broooo""")

login3()
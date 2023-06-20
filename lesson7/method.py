
def printUsername(nama):
    print(nama)

def printNote(Note):
    print(Note)


def login():
    username = input("masukan username : ")
    password = input("masukan password : ")

    if username != "mumzz" != "123":
        print("Username salah brooo")
        return
    
    if username !=password != "123":
        print("password salah brooo")
        return
    
    print("Welcome Broooo !!!")

def Menu():
    print("""
                ============================
                A P L I K A S I - M U M Z Z 
                ============================
    ===========================================================
         MENU :     1. Login     2. Register     3. Exit
    ===========================================================
    """)

    menu = input("Masukin Menunnya : ")

    if menu == "1" :
        print("login")
        return
    
    if menu == "2" :
        print("register")
        return
    
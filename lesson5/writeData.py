#fileData = open("database.txt", "r")

writeData = open("database.txt", "a")

text = input("masukan text : ")

writeData.write(text + "\n")
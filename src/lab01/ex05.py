fio = input("ФИО: ")

parts = fio.split()

initials = "".join(word[0].upper() for word in parts) + "."

length = len(fio.replace(" ", ""))+2

print(f"Инициалы: {initials}")
print(f"Длина (символов): {length}")
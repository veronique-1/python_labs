fio = input("ФИО: ")

parts = fio.split()

initials = "".join(word[0].upper() for word in parts) + "."

length = len(fio.replace(" ", ""))

print(f"Инициалы: {initials}")
print(f"Длина (символов): {length}")
def format_record(rec: tuple[str, str, float]) -> str:
    
    if not isinstance(rec,tuple):
        raise TypeError
    if len(rec) != 3:
        raise ValueError("Запись должна содержать ровно 3 элемента")

    fio, group, gpa = rec

    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("ФИО и группа должны быть строками")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")

    fio_parts = fio.strip().split()
    group = group.strip()

    if not fio_parts:
        raise ValueError("ФИО не может быть пустым")
    if not group:
        raise ValueError("Группа не может быть пустой")
    if not (0.0 <= gpa <= 5.0):
        raise ValueError("GPA должен быть в диапазоне от 0.0 до 5.0")

    surname = fio_parts[0].capitalize()

    initials = ""
    for part in fio_parts[1:3]:
        if part:
            initials += part[0].upper() + "."

    gpa_str = f"{gpa:.2f}"

    return f"{surname} {initials}, гр. {group}, GPA {gpa_str}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-25", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна  сергеевна", "ABB-01", 3.999)))

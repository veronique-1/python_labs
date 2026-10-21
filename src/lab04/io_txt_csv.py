import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает текстовый файл и возвращает его содержимое одной строкой.

    Ошибки FileNotFoundError (если файла нет) и UnicodeDecodeError 
    (если кодировка не подходит) намеренно не перехватываются и 
    пробрасываются вызывающему коду.

    Args:
        path (str | Path): Путь к файлу.
        encoding (str): Кодировка файла. По умолчанию "utf-8". 
                        Пользователь может выбрать другую, например encoding="cp1251".

    Returns:
        str: Содержимое файла в виде одной строки.
    """
    p = Path(path)
    return p.read_text(encoding=encoding)
#-------------------------------------------------------------------------------------------

def ensure_parent_dir(path: str | Path) -> None:
    """
    Создаёт все родительские директории для указанного файла, если их ещё нет.

    Функция полезна перед записью в файл: если папки, в которой должен
    лежать файл, не существует, обычная запись упадёт с ошибкой
    FileNotFoundError. Вызов этой функции заранее решает проблему.

    Если папка уже существует - ошибка не выбрасывается, функция
    просто завершает работу.

    Args:
        path: путь к файлу (не к папке) — строка или объект Path.

    Returns:
        None.
    """
    p = Path(path)
    # parents=True  — создаёт все промежуточные папки в цепочке (a/b/c),
    #                 а не только последнюю.
    # exist_ok=True — не выбрасывает ошибку, если папка уже существует.
    p.parent.mkdir(parents=True, exist_ok=True)
    
#-------------------------------------------------------------------------------------------

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """
    Записывает строки в CSV-файл с разделителем «запятая».

    Существующий файл перезаписывается. Запись идёт через csv.writer,
    поэтому значения с запятыми и кавычками экранируются автоматически.
    Пустой rows без header создаёт пустой файл, с header — файл только
    с заголовком.

    Args:
        rows: строки таблицы; все должны быть одинаковой длины.
        path: путь к создаваемому файлу — строка или Path.
        header: заголовок таблицы; если None, заголовок не пишется.

    Returns:
        None.

    Raises:
        TypeError: если строка таблицы не список и не кортеж.
        ValueError: если строки в rows разной длины (или не совпадают с длиной header).
    """
    rows = list(rows)
    p = Path(path)
    # 1. Проверка типов строк (до открытия файла, чтобы не оставить битый csv).
    for row in rows:
        if not isinstance(row, (list, tuple)):
            raise TypeError(
                f"Строка таблицы должна быть списком или кортежем,а получен {type(row).__name__}.")

    # 2. Определяем эталонную длину строки.
    if not rows:
        standard = len(header) if header is not None else 0
    else:
        standard = len(rows[0]) if header is None else len(header)

    # 3. Проверка, что все строки одной длины.
    for i, row in enumerate(rows):
        if len(row) != standard:
            raise ValueError(
                f"Ошибка: строка {i} имеет длину {len(row)}, а ожидалась {standard}.")
            
    # 4. Создаём папки, если их нет.
    ensure_parent_dir(path)

    # 5. Запись в файл.
    with p.open("w", newline="", encoding="utf-8") as file:
        w = csv.writer(file)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
    
#-------------------------------------------------------------------------------------------

if __name__ == "__main__":
    ensure_parent_dir("data/lab04/input.txt")   # ← создаёт папку data/lab04
    Path("data/lab04/input.txt").write_text("Привет, мир, привет!!!", encoding="utf-8")
    txt = read_text("data/lab04/input.txt")
    print("Успешно прочитано")
    write_csv([("word", "count"), ("test", 3)], "data/lab04/check.csv")
    print("Файл создан")
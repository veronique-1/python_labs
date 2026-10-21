from src.lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir
from src.lib.text import normalize, tokenize, top_n, count_freq
from pathlib import Path


def generate_report(input_path: str | Path, output_path: str | Path, encoding: str = "utf-8"):
    """
    Читает текст, считает частоты слов и сохраняет отчет в CSV.
    Выводит краткое резюме в консоль.
    """
    # 1. Читаем текст, передаем кодировку
    text = read_text(input_path, encoding=encoding)
    
    # 2. Обрабатываем
    normal_text = normalize(text)     # нормализация (нижний регистр, ё->е)
    tokens = tokenize(normal_text)    # токенизация (разбиение на слова)
    freq = count_freq(tokens)         # подсчет частот (словарь {слово: частота})
    top_5 = top_n(freq, 5)            # топ-5 для консоли

    # 3. Записываем CSV (все отсортированные слова)
    ensure_parent_dir(output_path)   # создаем папку, если ее нет
    write_csv(top_5, output_path, header=("word", "count"))

    # 4. Выводим резюме в консоль
    total_words = len(tokens)    # всего слов (с повторами)
    unique_words = len(freq)     # уникальных слов (ключей в словаре)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_5:
        print(f"{word}:{count}")
    
#----------------------------------------------------------------------------------------

def run_test_a():
    '''Тест А: обычный файл с текстом'''
    print("\n" + "="*40)
    print("ТЕСТ А: Один файл")
    print("="*40)

    input_file = "data/lab04/input.txt"
    output_file = "data/lab04/report.csv"

    ensure_parent_dir(input_file)
    Path(input_file).write_text("Привет, мир, привет!!!", encoding = "utf-8")

    #Запускаем генерацию
    generate_report(input_file, output_file)

    #Проверяем CSV
    print("\n---Проверка report.csv---")
    actual_csv = read_text(output_file)
    expected_csv = "word,count\nпривет,2\nмир,1\n"
    if actual_csv==expected_csv:
        print("CSV совпадает с ожидаемым!")
    else:
        print("Ошибка! CSV не совпадает с ожидаемым")

def run_test_b_empty():
    '''Тест B: пустой файл'''
    print("\n" + "="*40)
    print("ТЕСТ B: Пустой файл")
    print("="*40)

    input_file = "data/lab04/empty.txt"
    output_file = "data/lab04/report_empty.csv"

    #Создаем пустой входной файл
    write_csv([],input_file)
    #Запускаем генерацию
    generate_report(input_file,output_file)

    #Проверяем CSV
    print("\n---Проверка report_empty.csv---")
    actual_csv = read_text(output_file)
    expected_csv = "word,count\n"
    if actual_csv==expected_csv:
        print("CSV корректен")
    else:
        print("CSV не совпадает")

def run_test_c():
    '''Тест С: кодировка cp1251'''
    print("\n" + "="*40)
    print("ТЕСТ С: кодировка cp1251")
    print("="*40)
    
    input_file = "data/lab04/input_cp1251.txt"
    output_file = "data/lab04/report_cp1251.csv"

    ensure_parent_dir(input_file)
    Path(input_file).write_text("Привет", encoding = "cp1251")

    print("---Запуск для cp1251---")
    generate_report(input_file,output_file,encoding="cp1251")
    print("--Результат в report_cp1251---")
    print(read_text(output_file))
                                
if __name__ == "__main__":
    run_test_a()
    run_test_b_empty()
    run_test_c()

# python3 -m src.lab04.text_report
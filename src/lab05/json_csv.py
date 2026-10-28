import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    ''' Преобразует JSON со списком словарей в CSV
    Отсутствующие поля заполняются пустой строкой.
    Порядок колонок - алфавитный.
    
    Raises:
        FileNotFoundError: входного файла нет
        ValueError: не то расширение, пустой файл или не список словарей
    '''
    json_file = Path(json_path)
    if not json_file.is_file():
        raise FileNotFoundError(f"Файл не найден: {json_path}")
    
    # Добавлена проверка расширения (требование ТЗ)
    if json_file.suffix.lower() != '.json':
        raise ValueError(f"Неверный тип файла. Ожидался .json, получен: {json_file.suffix}")

    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Неверный формат JSON или файл пуст")
    
    if not isinstance(data, list) or not data:
        raise ValueError('JSON должен содержать непустой список объектов (словарей)')
    if not all(isinstance(item, dict) for item in data):
        raise ValueError('Все элементы списка в JSON должны быть словарями')

    all_keys = set()
    for item in data:
        all_keys.update(item.keys())
    headers = sorted(list(all_keys))

    if not headers:
        raise ValueError('В JSON отсутствуют данные для создания колонок')
        
    try:
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except Exception as e:
        raise ValueError(f"Ошибка при записи CSV файла: {e}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    '''Преобразовать CSV в JSON со списком словарей
    Первая строка в CSV - заголовок

    Raises:
        FileNotFoundError: входного файла нет
        ValueError: не то расширение, нет заголовка или нет ни одной записи
    '''
    csv_file = Path(csv_path)
    if not csv_file.is_file():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")
        
    # Добавлена проверка расширения (требование ТЗ)
    if csv_file.suffix.lower() != '.csv':
        raise ValueError(f"Неверный тип файла. Ожидался .csv, получен: {csv_file.suffix}")

    try:
        with open(csv_file, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                raise ValueError('CSV-файл пуст или нет заголовка')
            data = list(reader)
        if not data:
            raise ValueError('CSV-файл не содержит данных (только заголовок)')
        
    except csv.Error as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    
    try:
        Path(json_path).parent.mkdir(parents=True, exist_ok=True)
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError as e:
        raise ValueError(f"Ошибка записи JSON: {e}")


if __name__ == "__main__":
    sample_json = "data/lab05/samples/people.json"
    out_csv = "data/lab05/out/people_from_json.csv"
    out_json = "data/lab05/out/people_from_csv.json"

    print("="*30)

    try:
        # ----------------------------------
        # JSON -> CSV
        # ----------------------------------
        print('Test 1: JSON -> CSV')
        with open(sample_json, 'r', encoding='utf-8') as f:
            j_len = len(json.load(f))
        json_to_csv(sample_json, out_csv)

        with open(out_csv, 'r', encoding='utf-8') as f:
            c_len = len(f.readlines()) - 1 # не считаем заголовок
        print(f"Записей JSON: {j_len}")
        print(f"Записей CSV:  {c_len}")

        assert j_len == c_len, 'Количество записей не совпадает!'
        print("Успешно!")

        print('-'*30)
        
        # -------------------------------------
        # CSV -> JSON
        # -------------------------------------
        print('Test 2: CSV -> JSON')
        csv_to_json(out_csv, out_json)
        with open(out_json, 'r', encoding='utf-8') as f:
            final_j_len = len(json.load(f))
        print(f"Записей CSV:  {c_len}")
        print(f"Записей JSON: {final_j_len}")

        assert c_len == final_j_len, 'Количество записей не совпадает!'
        print("Успешно!")

        print('='*30)
    except Exception as e:
        print(f"\nОшибка: {e}")


data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
path = Path("data/out/people1.json")

# Записываем данные в файл
with path.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Данные успешно записаны в {path}")

# Читаем данные обратно
with path.open(encoding="utf-8") as f:
    loaded_data = json.load(f)
    print("Прочитанные данные:", loaded_data)
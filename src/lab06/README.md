# python_labs
# ЛР6 — CLI‑утилиты с argparse (cat/grep‑lite + конвертеры)
## Модуль src/lab06/cli_text.py

Модуль реализует консольную утилиту для работы с текстовыми файлами с использованием argparse. Утилита предоставляет две подкоманды:

-stats — анализ частотности слов. Принимает обязательный аргумент --input (путь к файлу) и опциональный --top (количество выводимых слов, по умолчанию 5). Функция run_stats читает файл, нормализует текст, разбивает его на токены, подсчитывает частоту и выводит общее количество слов, число уникальных слов и список самых частых слов с их количеством.

-cat — построчный вывод содержимого файла. Принимает --input и флаг -n (включает нумерацию строк). Функция run_cat использует splitlines() для корректного разбиения текста на строки без лишних переносов.

Организация парсинга: в функции main() создается ArgumentParser с подпарсерами через add_subparsers(dest="command", required=True). Выбранная команда сохраняется в args.command, после чего через if/elif вызывается соответствующая функция.

Обработка ошибок: перед выполнением проверяется, что --top больше нуля. Блок выполнения обернут в try/except, перехватывающий FileNotFoundError и UnicodeDecodeError. Все ошибки выводятся через parser.error() — в понятном виде, без стектрейса.

Переиспользование кода: модуль не дублирует логику — используется read_text из ЛР4 и функции normalize, tokenize, count_freq, top_n из вспомогательного модуля.

``` python
import argparse

from src.lab04.io_txt_csv import read_text
from src.lib.text import count_freq, normalize, tokenize, top_n


def run_stats(path: str, top: int) -> None:
    """Напечатать число слов и топ самых частых."""
    tokens = tokenize(normalize(read_text(path)))
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{top}:")
    for word, count in top_n(freq, top):
        print(f"{word}: {count}")


def run_cat(path: str, numbered: bool) -> None:
    """Напечатать файл построчно, с номерами строк если numbered=True."""
    lines = read_text(path).splitlines()
    for number, line in enumerate(lines, start=1):
        if numbered:
            print(f"{number}: {line}")
        else:
            print(line)


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description="Текстовые утилиты: статистика слов и вывод файла"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    stats_parser = sub.add_parser("stats", help="частоты слов в тексте")
    stats_parser.add_argument("--input", required=True, help="текстовый файл")
    stats_parser.add_argument("--top", type=int, default=5, help="сколько слов показать")

    cat_parser = sub.add_parser("cat", help="вывести файл построчно")
    cat_parser.add_argument("--input", required=True, help="файл для вывода")
    cat_parser.add_argument("-n", action="store_true", help="нумеровать строки")

    args = parser.parse_args(argv)

    if args.command == "stats" and args.top < 1:
        parser.error("--top должен быть положительным числом")

    try:
        if args.command == "stats":
            run_stats(args.input, args.top)
        elif args.command == "cat":
            run_cat(args.input, args.n)
    except FileNotFoundError:
        parser.error(f"файл не найден: {args.input}")
    except UnicodeDecodeError:
        parser.error(f"файл {args.input} не читается в кодировке UTF-8")


if __name__ == "__main__":
    main()
```
## Выводы
### cat — вывод файла
```
python -m src.lab06.cli_text cat --input data/lab05/samples/people.csv -n
python -m src.lab06.cli_text cat --input data/lab05/samples/people.csv -n
```
Файл читается в UTF-8. С флагом `-n` каждая строка получает номер в формате `1: содержимое строки`.

![фото](../../images/lab06/v1.png)

### stats — частоты слов
![фото](../../images/lab06/m.png)
```
python -m src.lab06.cli_text stats --input data/lab06/samples/moscow.txt
python -m src.lab06.cli_text stats --input data/lab06/samples/moscow.txt --top 3 
```
Результат выводится в формате «слово — табуляция — количество», по убыванию частоты; при равной частоте — по алфавиту. Если разных слов меньше, чем `N`, выводятся все имеющиеся. Значение `--top` должно быть положительным целым числом.

![фото](../../images/lab06/v2.png)

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
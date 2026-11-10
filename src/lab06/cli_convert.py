import argparse
import os

from src.lab05.csv_xlsx import csv_to_xlsx
from src.lab05.json_csv import csv_to_json, json_to_csv


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Конвертеры данных между JSON, CSV и XLSX"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # У всех трёх команд одинаковые флаги: откуда читать и куда писать.
    # dest нужен, потому что args.in — синтаксическая ошибка (in — ключевое слово).
    json2csv_parser = sub.add_parser("json2csv", help="JSON -> CSV")
    json2csv_parser.add_argument("--in", dest="input", required=True, help="входной JSON")
    json2csv_parser.add_argument("--out", dest="output", required=True, help="выходной CSV")

    csv2json_parser = sub.add_parser("csv2json", help="CSV -> JSON")
    csv2json_parser.add_argument("--in", dest="input", required=True, help="входной CSV")
    csv2json_parser.add_argument("--out", dest="output", required=True, help="выходной JSON")

    csv2xlsx_parser = sub.add_parser("csv2xlsx", help="CSV -> XLSX")
    csv2xlsx_parser.add_argument("--in", dest="input", required=True, help="входной CSV")
    csv2xlsx_parser.add_argument("--out", dest="output", required=True, help="выходной XLSX")

    args = parser.parse_args()

    # Создаём папку для результата, если её ещё нет (например, data/out/)
    out_dir = os.path.dirname(args.output)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir)

    try:
        if args.command == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
    except FileNotFoundError:
        parser.error(f"файл не найден: {args.input}")
    except ValueError as error:
        # текст ошибки берём из функций ЛР5, там он уже понятный
        parser.error(str(error))

    print(f"Готово: {args.input} -> {args.output}")


if __name__ == "__main__":
    main()
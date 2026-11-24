import random
import timeit
import csv
from src.lab04.io_txt_csv import write_csv
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast


def format_time(seconds):
    """Красиво форматируем время для таблицы."""
    if isinstance(seconds, str):
        return seconds
    return f"{seconds:.4f} с" if seconds < 60 else "> 60 с"


def print_row(task, n, impl, seconds):
    """Вспомогательная функция для красивого вывода строки."""
    # Если seconds - это строка (например, '>60'), выводим как есть, иначе форматируем
    val = seconds if isinstance(seconds, str) else format_time(seconds)
    print(f"{task:<10} | {n:<7} | {impl:<15} | {val:<12}")


def run_benchmark():
    random.seed(42)  # Чтобы при каждом запуске генерировались одни и те же данные
    csv_results = []
    headers = ["task", "n", "impl", "seconds"]

    print("\nРезультаты бенчмарка:")
    print(f"{headers[0]:<10} | {headers[1]:<7} | {headers[2]:<15} | {headers[3]:<12}")
    print("-" * 55)

    sizes_sort = [1000, 10000, 100000]

    for n in sizes_sort:
        data = [random.randint(-1000, 1000) for _ in range(n)]

        # Встроенная сортировка (эталон)
        t_sorted = timeit.timeit(lambda: sorted(data), number=1)
        print_row("sorting", n, "sorted", t_sorted)
        csv_results.append(("sorting", n, "sorted", t_sorted))

        for fn, name in [(bubble_sort, "bubble"), (insertion_sort, "insertion"), (selection_sort, "selection")]:
            if n >= 100000:
                print_row("sorting", n, name, ">60")
                csv_results.append(("sorting", n, name, ">60"))
                continue
            
            # Важно: передаем копию data.copy(), чтобы исходные данные не менялись
            t = timeit.timeit(lambda: fn(data.copy()), number=1)
            print_row("sorting", n, name, t)
            csv_results.append(("sorting", n, name, t))

    n_search = 100000
    search_data = [random.randint(-10000, 10000) for _ in range(n_search)]
    search_sorted = sorted(search_data)
    queries = [random.randint(-10000, 10000) for _ in range(10000)]

    # Линейный поиск
    t_linear = timeit.timeit(lambda: [linear_search(search_data, x) for x in queries], number=1)
    print_row("search", n_search, "linear_search", t_linear)
    csv_results.append(("search", n_search, "linear_search", t_linear))

    # Бинарный поиск (включая сортировку)
    def sort_and_search():
        s_data = sorted(search_data)
        for x in queries:
            binary_search(s_data, x)
    t_binary = timeit.timeit(sort_and_search, number=1)
    print_row("search", n_search, "binary_search", t_binary)
    print(" " * 36 + "(вкл. сортировку)") # Подпись под таблицей
    csv_results.append(("search", n_search, "binary_search", t_binary))

    for n in [1000, 10000]:
        nums = [random.randint(0, n) for _ in range(n)]
        # Делаем так, чтобы правильная пара лежала в самом конце,
        # иначе brute найдет её моментально и покажет 0.0000
        nums[-2:] = [-1, -2]
        target = -3

        t_brute = timeit.timeit(lambda: two_sum_brute(nums, target), number=1)
        print_row("two_sum", n, "two_sum_brute", t_brute)
        csv_results.append(("two_sum", n, "two_sum_brute", t_brute))

        t_fast = timeit.timeit(lambda: two_sum_fast(nums, target), number=1)
        print_row("two_sum", n, "two_sum_fast", t_fast)
        csv_results.append(("two_sum", n, "two_sum_fast", t_fast))

    print("\n---Сохранение данных---")
    try:
        # Для записи в CSV мы не можем передать строку ">60" в поле float,
        # поэтому просто передаем как есть, write_csv должен обработать.
        write_csv(rows=csv_results, path="data/lab07/bench.csv", header=tuple(headers))
        print("Результаты сохранены в data/lab07/bench.csv")
    except Exception as e:
        print(f"Ошибка сохранения CSV: {e}")
        print("Данные, которые не удалось сохранить:")
        for row in csv_results:
            print(row)


if __name__ == "__main__":
    run_benchmark()

# python -m src.lab07.bench
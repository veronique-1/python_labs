import random
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

def check_sorting(fn, trials: int = 100) -> int:
    """Проверяет функцию сортировки на случайных данных против эталонного sorted().
    Принимает конкретную функцию для проверки и кол-во испытаний (по умолчанию 100).
    Возвращает кол-во успешно пройденных тестов.
    """
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: получено {result}, ожидалось {sorted(nums)}"
        assert nums == original, f"{fn.__name__} изменила исходный список"
    return trials

def check_search(trials: int = 100) -> int:
    """Проверяет функции linear_search и binary_search на случайных данных.
    Возвращает количество успешно пройденных испытаний.
    """
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-50, 50) for _ in range(n)]
        x = random.randint(-60, 60)

        # Линейный поиск против list.index
        try:
            expected_lin = nums.index(x)
        except ValueError:
            expected_lin = -1  # если числа нет, то правильный ответ(эталон) = -1
        
        actual_lin = linear_search(nums, x)
        assert actual_lin == expected_lin, f"linear_search ошиблась для поиска {x} в {nums}: получено {actual_lin}, ожидалось {expected_lin}"

        # Бинарный поиск
        sorted_nums = sorted(nums)
        try:
            expected_bin = sorted_nums.index(x)
        except ValueError:
            expected_bin = -1
            
        actual_bin = binary_search(sorted_nums, x)
        if expected_bin == -1:
            assert actual_bin == -1, f"binary_search не нашла элемент, которого нет: {x} в {sorted_nums}"
        else:
            assert actual_bin != -1 and sorted_nums[actual_bin] == x, f"binary_search вернула некорректный индекс {actual_bin} для {x} в {sorted_nums}"

    # Редкие случаи (граничные условия)
    assert binary_search([], 5) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([5], 7) == -1
    assert binary_search([1, 3], 3) == 1

    return trials

def check_two_sum(trials: int = 100) -> int:
    """Проверяет эквивалентность результатов two_sum_brute и two_sum_fast.
    Возвращает количество успешно пройденных тестов.
    """
    for _ in range(trials):
        n = random.randint(2, 30)
        nums = [random.randint(-30, 30) for _ in range(n)]
        target = random.randint(-50, 50)

        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)

        # Если медленный ничего не нашел, то быстрый тоже
        if res_brute is None:
            assert res_fast is None, f"two_sum_brute не нашла, а fast нашла {res_fast} для nums={nums}, target={target}"
            continue
        
        # Если медленный нашел, то быстрый тоже должен найти
        assert res_fast is not None, f"two_sum_brute нашла {res_brute}, fast не нашла для nums={nums}, target={target}"

        # Если нашли, проверяем сумму для обоих
        i, j = res_brute
        assert nums[i] + nums[j] == target, f"brute вернул неверные индексы: {res_brute}"
        i, j = res_fast
        assert nums[i] + nums[j] == target, f"fast вернул неверные индексы: {res_fast}"
        
    return trials 

if __name__ == "__main__":
    random.seed(42)  # одни и те же случайные данные для всех алгоритмов
    
    total = 0
    for fn in (bubble_sort, insertion_sort, selection_sort):
        total += check_sorting(fn, trials=100)
        
    total += check_search()
    total += check_two_sum()

    print(f"OK: {total} проверок")

# python -m src.lab07.check
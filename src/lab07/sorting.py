def bubble_sort(nums: list[int]) -> list[int]:
    """Новый список, отсортированный по возрастанию. Исходный не меняется.
    Флаг flag дает ранний выход.
 
    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([2, 2, 1]) -> [1, 2, 2]
    bubble_sort([]) -> []
    """
    a = list(nums)
    n = len(a)
    for i in range(n):
        flag = False
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = True
        if not flag:
            break
    return a

def insertion_sort(nums: list[int]) -> list[int]:
    """Сортирует список методом вставок.
    Создает и возвращает новый отсортированный список, не меняя исходный.
    Принимает исходный, возвращает новый.
    """
    a = list(nums)
    for i in range(1,len(a)):
        key = a[i]
        j = i - 1
        while j>=0 and a[j]>key:
            a[j + 1] = a[j]
            j-=1 
        a[j + 1] = key
    return a

def selection_sort(nums: list[int]) -> list[int]:
    """Сортирует список методом выбора.
    Создает и возвращает новый отсортированный список, не изменяя исходный.
    Принимает исходный, возвращает новый.
    Сложность O(n^2)
    """
    a = list(nums)
    n = len(a)
    for i in range(n):
        minidx = i
        for j in range(i + 1, n):
            if a[j] < a[minidx]:
                minidx = j
        a[i], a[minidx] = a[minidx], a[i]
    return a

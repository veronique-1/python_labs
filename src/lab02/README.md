# python_labs
# Лабораторная работа 2
# Задание A1

## Реализуем функцию поиска минимума и максимума в списке. Сначала проверяем список на пустоту (вызываем ошибку ValueError, если он пуст). Инициализируем минимальное и максимальное значения первым элементом списка. Затем в цикле перебираем оставшиеся числа: если число меньше текущего минимума — обновляем минимум, если больше максимума — обновляем максимум. Возвращаем кортеж из двух значений.

```python 

def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError
    
    min_val = max_val = nums[0]

    for num in nums[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val
```
![фото](../../images/lab02/exA1.png)
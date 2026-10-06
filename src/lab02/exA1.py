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

print( min_max([3, -1, 5, 5, 0]))
print( min_max([42]))
print( min_max([-5, -2, -9]))
print( min_max([1.5, 2, 2.0, -3.1]))
print( min_max([]))
def unique_sorted(nums: list[float | int]) -> list[float | int]:

    uni_nums = []
    for num in nums:
        if num not in uni_nums:
            uni_nums.append(num)
    n = len(uni_nums)
    for i in range(n):
        for j in range(n-i-1):
            if uni_nums[j]>uni_nums[j+1]:
                uni_nums[j],uni_nums[j+1]=uni_nums[j+1],uni_nums[j]
    return uni_nums

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
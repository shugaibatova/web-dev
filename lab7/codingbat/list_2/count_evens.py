def count_evens(nums):
    sum = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            sum += 1
    return sum


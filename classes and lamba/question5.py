def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])

    return result


print(three_sum([-25, -10, -7, -3, 2, 4, 8, 10]))
class TwoSum:
    def find_indices(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i+1, j+1


t = TwoSum()
target = 50
nums = [90, 20, 10, 40, 50, 60, 70]
print(t.find_indices(nums, target))

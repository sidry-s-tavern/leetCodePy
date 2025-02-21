class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
        return [-1,-1]


print(Solution.twoSum(Solution, [1, 4, 7], 11))

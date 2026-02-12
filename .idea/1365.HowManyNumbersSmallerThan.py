class Solution:
    def printResult(nums: list[int]):
        print(Solution.smallerNumbersThanCurrent(Solution, nums))

    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            result.append(0)
            for j in nums:
                if j < nums[i]:
                    result[i] = result[i] + 1
        return result


Solution.printResult([4,5,1,2,3])

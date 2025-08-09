from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftSum, rightSum = 1, 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = leftSum
            leftSum *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= rightSum
            rightSum *= nums[i]

        return result


print(Solution().productExceptSelf([1, 2, 3, 4]))

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        current = 0
        result = []

        while current < len(nums):
            start = nums[current]

            while current < len(nums) - 1 and nums[current] == nums[current + 1] - 1:
                current += 1

            end = nums[current]
            if start == end:
                result.append(f'{start}')
            else:
                result.append(f'{start}->{end}')

            current += 1

        return result


print(Solution().summaryRanges(nums=[0, 1, 2, 4, 5, 7]))

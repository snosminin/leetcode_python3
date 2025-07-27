from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_set = set()

        for index, num in enumerate(nums):
            if num in nums_set:
                return True

            nums_set.add(num)

            if index >= k:
                nums_set.remove(nums[index - k])

        return False

print(Solution().containsNearbyDuplicate([1,2,3,1], 3))

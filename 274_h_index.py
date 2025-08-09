from typing import List


class Solution:
    @staticmethod
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        i = 0
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        return i + 1

print(Solution().hIndex([11,15]))

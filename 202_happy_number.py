class Solution:
    numberSquareMap: dict[int, int] = {
        0: 0,
        1: 1,
        2: 4,
        3: 9,
        4: 16,
        5: 25,
        6: 36,
        7: 49,
        8: 64,
        9: 81
    }

    @staticmethod
    def sum(n: int) -> int:
        result = 0
        while n > 0:
            result += Solution.numberSquareMap[n % 10]
            n //= 10
        return result

    def isHappy(self, n: int) -> bool:
        slow = self.sum(n)
        fast = self.sum(self.sum(n))

        while slow != fast:
            slow = self.sum(slow)
            fast = self.sum(self.sum(fast))

        return slow == 1


print(Solution().isHappy(n=19))

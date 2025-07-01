class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []
        aPointer, bPointer = len(a) - 1, len(b) - 1
        while aPointer >= 0 or bPointer >= 0:
            aBit = int(a[aPointer]) if aPointer >= 0 else 0
            bBit = int(b[bPointer]) if bPointer >= 0 else 0

            carry, divResult  = divmod(aBit + bBit + carry, 2)
            result.insert(0, divResult)

            if(aPointer >= 0): aPointer-=1
            if(bPointer >= 0): bPointer-=1

        if carry == 1:
            result.insert(0, carry)
        return "".join(str(n) for n in result)

print(Solution().addBinary(a = "11",b = "1"))
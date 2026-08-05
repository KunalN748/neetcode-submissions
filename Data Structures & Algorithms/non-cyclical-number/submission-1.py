class Solution:
    def isHappy(self, n: int) -> bool:
        arr = []
        dSquare = 0
        while dSquare != 1:
            dSquare = 0
            digits = [int(d) for d in str(n)]
            for i in range(len(digits)):
                dSquare += (digits[i] * digits[i])
            if dSquare in arr:
                return False
            n = dSquare
            arr.append(n)
        return True
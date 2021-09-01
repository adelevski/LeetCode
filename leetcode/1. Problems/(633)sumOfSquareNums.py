


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        base = math.floor(math.sqrt(c))

        for a in range(base+1):  # loop all possible number a
            b = c - a**2  # another possible number b
            b_sqrted = math.sqrt(b)
            if b_sqrted - int(b_sqrted) == 0:  # means sqrt(b) cannot be an integer
                return True
        return False
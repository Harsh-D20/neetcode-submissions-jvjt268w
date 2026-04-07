class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            new_n = 0
            for d in str(n):
                new_n += int(d) * int(d)
            if new_n == 1:
                return True
            n = new_n
        return False
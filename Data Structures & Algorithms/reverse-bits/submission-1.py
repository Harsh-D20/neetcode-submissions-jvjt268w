class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
        queue = []
        while n > 0:
            if n & 1 == 1:
                queue.append(1)
            else:
                queue.append(0)
            n = n >> 1

        out = queue.pop(0)
        zero_pad = 31 - len(queue)
        while queue:
            out = out << 1
            if queue.pop(0) == 1:
                out = out | 1
        out = out << zero_pad
        return out


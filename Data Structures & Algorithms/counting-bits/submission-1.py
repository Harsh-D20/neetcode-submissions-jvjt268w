class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: 
            return [0]
        if n == 1:
            return [0,1]
        if n == 2:
            return [0,1,1]
        out = [0 for _ in range(n+1)]
        out[0] = 0
        out[1] = 1
        out[2] = 2

        for i in range(2, n+1):
            if i % 2 == 0:
                out[i] = out[i // 2]
            else:
                out[i] = out[i // 2] + 1
        
        return out
        
        # 0 => 0
        # 1 => 1
        # 2 => 10
        # 3 => 11
        # 4 => 100
        # 5 => 101
        # 6 => 110
        # 7 => 111
        # 8 => 1000
        # 10 => 1010
        # 12 => 1100
        # 16 => 10000
        # 20 => 10100

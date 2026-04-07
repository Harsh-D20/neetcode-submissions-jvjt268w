from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        c = Counter(nums)
        for _ in range(k): 
            max_count = 0
            max_n = None
            for n,count in c.items():
                if count > max_count:
                    max_count = count
                    max_n = n
            out.append(max_n)
            del c[max_n]
        return out


            

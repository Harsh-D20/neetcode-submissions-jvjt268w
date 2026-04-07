from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_with_freqs = [None for _ in range(len(nums)+1)]
        freqs = {}
        for num in nums: 
            if num in freqs: 
                freqs[num] += 1
            else:
                freqs[num] = 1
        for n,f in freqs.items():
            if nums_with_freqs[f] == None:
                nums_with_freqs[f] = [n]
            else:
                nums_with_freqs[f].append(n)

        out = []
        for nums in nums_with_freqs[::-1]: 
            if nums == None: 
                continue
            while k > 0 and nums != []:
                out.append(nums.pop())
                k -= 1
        return out


            

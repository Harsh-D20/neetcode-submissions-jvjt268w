class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        p_set = [[]]
        for n in nums:
            p_set += [s + [n] for s in p_set]
        return p_set
                

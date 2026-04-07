class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        p_set = []
        p_set.append([])
        print(p_set, len(p_set))
        for n in nums:
            to_add = []
            for s in p_set:
                to_add.append(s + [n])
            p_set += to_add
        return p_set
                

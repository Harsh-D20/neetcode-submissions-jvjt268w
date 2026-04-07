class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        bit = 0
        for n in range(len(nums)+1):
            bit ^= n
        
        for n in nums:
            bit ^= n
        
        return bit
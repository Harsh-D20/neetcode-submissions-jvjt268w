class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r = len(nums)
        bit = 0
        for n in range(r+1):
            bit ^= n
        
        for n in nums:
            bit ^= n
        
        return bit
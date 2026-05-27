class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # mask is n-digit bit "string", O(1)
        n = len(nums) - 1
        mask = 0 << (n - 1)
        for nm in nums:
            if (mask >> (nm-1)) & 1 == 1:
                return nm
            else:
                mask = mask | 1 << (nm-1)
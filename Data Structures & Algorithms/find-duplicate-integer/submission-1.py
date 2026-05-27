class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # mask is n-digit bit "string", O(1)
        n = len(nums) - 1
        mask = 0 << (n - 1)
        for nm in nums:
            # if the bit for nm is 1, we have seen it already
            if (mask >> (nm-1)) & 1 == 1:
                return nm
            else:
                # turn on the bit for nm
                mask = mask | 1 << (nm-1)
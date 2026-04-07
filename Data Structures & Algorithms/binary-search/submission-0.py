class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            idx = left + ((right - left) // 2)
            mid = nums[idx]
            if target > mid:
                left = idx + 1
            elif target < mid:
                right = idx - 1
            else: 
                return idx

        return -1
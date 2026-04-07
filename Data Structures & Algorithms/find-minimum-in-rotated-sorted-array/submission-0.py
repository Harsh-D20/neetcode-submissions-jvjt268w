class Solution:
    def findMin(self, nums: List[int]) -> int:
        out = nums[0]
        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] < nums[right]:
                out = min(out, nums[left])
                break
            mid = (left + right) // 2;
            out = min(out, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return out
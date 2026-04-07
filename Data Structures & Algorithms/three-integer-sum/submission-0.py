class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        for idx,val in enumerate(nums):
            if val > 0:
                break
            if idx > 0 and val == nums[idx - 1]:
                continue
            
            left, right = idx + 1, len(nums)-1
            while left < right:
                tsum = val + nums[left] + nums[right]
                if tsum > 0: 
                    right -= 1
                elif tsum < 0:
                    left += 1
                else:
                    out.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return out
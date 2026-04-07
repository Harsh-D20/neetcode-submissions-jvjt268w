class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = 1
        right_product = 1
        for n in nums[1:]:
            right_product *= n
        
        out = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            out[i] = int(left_product * right_product)
            if i < len(nums)-1:
                if nums[i+1] != 0:
                    right_product /= nums[i+1]
                else:
                    right_product = 1
                    for n in nums[i+2:]:
                        right_product *= n
            left_product *= nums[i]
        return out
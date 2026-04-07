class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        for i in range(len(digits)-1, -1, -1):
            cur_digit = digits[i] + carry
            print(cur_digit)
            if cur_digit >= 10:
                carry = cur_digit // 10
                digits[i] = cur_digit % 10
            else:
                digits[i] = cur_digit
                carry = 0
                break
        if carry: 
            return [carry] + digits
        return digits
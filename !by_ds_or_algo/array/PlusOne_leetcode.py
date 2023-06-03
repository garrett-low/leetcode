class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for idx,num in reversed(list(enumerate(digits))):
            digits[idx] = (num + 1) % 10
            if num != 9:
                break
            if idx == 0:
                digits.insert(0,1)
                
                
        return digits
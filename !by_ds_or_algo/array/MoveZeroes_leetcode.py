class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left] = nums[i]
                left += 1
        
        for i in range(left, len(nums)):
            nums[i] = 0

class SolutionWhatIsThisCrap(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        swappedZero = False
        left = 0
        right = len(nums) - 1
        
        while left < right:
#             print(nums)
#             print("left: ", left," right: ", right)
            if nums[left] == 0:
                for j in range (left, right):
                    temp = nums[j + 1]
                    if temp == 0:
                        swappedZero = True
                    nums[j + 1] = nums[j]
                    nums[j] = temp
#                     print("temp: ", temp)
                if swappedZero:
                    left -= 1
                    swappedZero = False
#                     print("left_2: ", left," right_2: ", right)
                right -= 1
#                 print("left_3: ", left," right_3: ", right)
            
            left += 1
#             print("left_4: ", left," right_4: ", right)
                
                
x = Solution()
a = [0,0,1]
x.moveZeroes(a)
print("a: ", a)

b = [0,0,0]
x.moveZeroes(b)
print("b: ", b)
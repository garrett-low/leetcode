class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dict = {}
        
        for idx, num in enumerate(nums):
           dict[num] = idx
           
        for i, num in enumerate(nums):
            find = target - num
            if find in dict and i != dict[find]:
                return [i, dict[find]]
        

class SolutionBruteForce(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for idx, num in enumerate(nums):
            find = target - num
            for j, pair in enumerate(nums):
                if idx == j:
                    pass
                if find == pair:
                    return [idx, j]
                
a = [2,7,11,15]
b = 9
x = SolutionBruteForce()
print(x.twoSum(a, b))

y = Solution()
print(y.twoSum(a,b))

c = [3,4,5,6,1,1]
d = 2
print(y.twoSum(c,d))

e = [3,2,4]
f = 6
print(y.twoSum(e,f))
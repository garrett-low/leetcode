# naive

# naive, doesn't satisfy constant memory
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        new_ary = [] # type: List[int]
        for num in nums:
            if num in new_ary:
                new_ary.remove(num)
            else:
                new_ary.append(num)
            
        return new_ary[0]

x = Solution()
a = [1,1,2,2,3,3,4]
print(x.singleNumber(a))
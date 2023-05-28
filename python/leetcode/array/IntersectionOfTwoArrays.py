# naive
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        inter = [] # type: List[int]
        
        for num_a in nums1:
            for num_b in nums2:
                if num_a == num_b:
                    inter.append(num_a)
                    nums2.remove(num_b)
                    break;
                
        return inter

a = [1,2,2,1]
b = [2,2]
x = Solution()
print(x.intersect(a, b))
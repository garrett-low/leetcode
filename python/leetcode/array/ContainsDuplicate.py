# use a hash table or set

# sort
class SolutionSort(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        nums = self.mergeSort(nums)
        
        for idx, val in enumerate(nums[1:], start=1):
            if (nums[idx-1] == val):
                return True
            
        return False
        
    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        
        nums_first = self.mergeSort(nums[:(len(nums)//2)])
        nums_second = self.mergeSort(nums[(len(nums)//2):])
        
        merge_nums = []
        
        while (nums_first and nums_second):
            if (nums_first[0] < nums_second[0]):
                merge_nums.append(nums_first[0])
                nums_first.pop(0)
            else:
                merge_nums.append(nums_second[0])
                nums_second.pop(0)
        
        while (nums_first):
            merge_nums.append(nums_first[0])
            nums_first.pop(0)
            
        while (nums_second):
            merge_nums.append(nums_second[0])
            nums_second.pop(0)
        
        return merge_nums

# naive
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        uniq_nums = []
        has_found_dup = False
        
        for num in nums:
            for uniq_num in uniq_nums:
                if num == uniq_num:
                    has_found_dup = True
                    break
            
            if not has_found_dup:
                uniq_nums.append(num)
            
            has_found_dup = False
        
        print(uniq_nums)
        
        if len(uniq_nums) < len(nums):
            return True
        else:
            return False
        
# x = Solution()
# nums = [1,2,3,1]
# print(x.containsDuplicate(nums))

x = SolutionSort()
nums = [1,2,3,1]
# print(x.mergeSort(nums))
print(x.containsDuplicate(nums))
nums = [1,2,3,4]
print(x.containsDuplicate(nums))
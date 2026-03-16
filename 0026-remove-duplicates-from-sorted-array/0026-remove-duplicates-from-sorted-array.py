class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low  = 0
        high =1 
        unique = 1

        while (high < len(nums)) :
            if (nums[high]==nums[low]):
                high+=1
                continue
            else :
                nums[low+1]=nums[high]
                low+=1
                high+=1
                unique+=1
        return unique   
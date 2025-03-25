class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # myset = set(range(1,len(nums)+1))
        
        # return list(myset - set(nums))

        return(list(set(range(1, len(nums) + 1)) - set(nums)))
        

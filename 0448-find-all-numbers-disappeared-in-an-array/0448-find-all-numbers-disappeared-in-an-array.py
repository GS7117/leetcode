class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        myset = set()
        for i in range (1,len(nums)+1) :
            myset.add(i)

        return list(myset - set(nums))
        

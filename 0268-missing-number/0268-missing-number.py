class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i,v in enumerate(nums) :
            if (i!= v) :
                return i

            if v== len(nums)-1 :
                return v+1
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        finalSum = nums[0]
        sum = 0
        for x in nums :
            sum = sum + x
            finalSum = max(sum , finalSum)
            if sum < 0:
                sum = 0

            


        return finalSum
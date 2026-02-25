class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        final =[0]*n
        left_result=[1]*n
        right_result=[1]*n
    

        for i in range(1, n) :
            left_result[i]= nums[i-1]*left_result[i-1]
            
        
        for i in range (n-2,-1,-1):
            right_result[i] = nums[i+1]*right_result[i+1]
            
        
        for i in range (n):
            final[i] = left_result[i]*right_result[i]
            
        
        return final
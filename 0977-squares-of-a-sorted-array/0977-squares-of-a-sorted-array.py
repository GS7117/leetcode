class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
      """
        split=0
        j=0
        i=0
        id = 0
        result = [None]*len(nums)
        for split in range(len(nums)):
            if nums[split]>=0:
                j=split
                i=split-1
                
                break
            else :
                j=len(nums)
                i = len(nums)-1

        while (i>=0 and j<len(nums)):
            if(nums[i]*nums[i] < nums[j]*nums[j]):
                result[id] = nums[i]*nums[i]
                i-=1
                id+=1
            else : 
                result[id] = nums[j]*nums[j]
                j+=1
                id+=1
        while(j<len(nums)):
            result[id]=nums[j]*nums[j]
            id+=1
            j+=1
        
        while(i>=0):
            result[id] = nums[i]*nums[i]
            id+=1
            i-=1
        
        return result
        
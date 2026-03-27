class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = 0
        total = 0
        subarray_size = float('inf')

        while(high<len(nums)) :
            total = total + nums[high]

            while (total >= target) : 
                total =  total -  nums[low]
                window_size = high - low + 1
                subarray_size = min(subarray_size, window_size)
                low+=1

            high+=1
            
                
                
        
        if subarray_size == float('inf') :
            return 0
        
        return subarray_size



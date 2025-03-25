class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myset = set()
        
        for i in range(len(nums)) :
            n = target - nums[i]
            if n in myset : 
                index = nums.index(n,0,i)
                return [index, i]
            else : 
                myset.add(nums[i])

            
                
                
            
           

        
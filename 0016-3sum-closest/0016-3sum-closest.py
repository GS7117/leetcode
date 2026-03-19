class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        difference = float('inf')
        res = 0
        nums.sort()
        if len(nums) == 3 :
            return sum([x for x in nums ])
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1

        

            while(left<right) :
                total = nums[i]+nums[left] + nums[right]
            
                
                if (total == target) :
                    return target
                
                elif (total < target): 
                    
                    if abs(target-total) < abs(difference) : 
                        difference  = target-total 
                        res = total
                    left+=1
                else : 
                    if abs(target-total) < abs(difference) :  
                        difference  = target-total
                        res = total
                    right-=1
                
        return res   
        
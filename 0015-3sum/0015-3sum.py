class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(0,len(nums)-2):
            if nums[i] > 0 :
                break

            if(i>0 and nums[i]==nums[i-1]):
                continue

            j = i+1
            k = len(nums)-1
            
            while (j < k):

                if(nums[i]==-(nums[j]+nums[k])):
                    res.append([nums[i], nums[j], nums[k]])
                    
                    j+=1
                    k-=1
                    
                    while (j < len(nums) and nums[j]==nums[j-1]):
                        j+=1
                    
                    while (k>=0 and nums[k]== nums[k+1]):
                        k-=1
                        
                elif(nums[i]<-(nums[j]+nums[k])):
                    j+=1
                
                else :
                    k-=1
        return res
   
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        myList = sorted(nums)
        
        thisDict = {}
        List1 = []
        for ind, val in enumerate(myList):
            if val not in thisDict.keys() : 
                thisDict[val] = ind
            
        for i in nums : 
            List1.append(thisDict[i])
        
        return List1
            

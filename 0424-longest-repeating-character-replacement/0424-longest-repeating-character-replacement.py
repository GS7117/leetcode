class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        low = 0
        high = 0
        res = 0
        length = 0
        total = len(s)
        a={}
        diff = 0
        for high in range(total) :
            
            a[s[high]]= a.get(s[high],0)+1
            maxCount = max(a.values())
            length = high - low +1
            diff= length-maxCount
            
            while (diff > k) :
                a[s[low]]-=1
                low+=1
                maxCount = max(a.values())
                length = high - low +1
                diff = length - maxCount

            length = high - low +1
            res = max(res,length)
        return res
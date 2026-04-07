class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        low = 0
        high = 0
        res = 0
        d = {}
        for high in range(len(fruits)) :
            d[fruits[high]] =  d.get(fruits[high],0)+1
            
            while(len(d) > 2) :
                d[fruits[low]]-=1
                if d[fruits[low]]==0 :
                    del d[fruits[low]]
                low+=1
            
            if len(d)<=2 : 
                no_Of_Fruits= high - low + 1
                res = max(res, no_Of_Fruits)

        return res
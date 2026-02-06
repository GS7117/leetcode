class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        l2 = []
        for i in range (len(candies)) :
            l2.append(bool(candies[i] + extraCandies >= max(candies)))
        return l2
        
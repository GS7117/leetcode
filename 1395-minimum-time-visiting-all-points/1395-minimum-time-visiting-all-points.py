class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0

        for i in range(1,len(points)) :
            start_point = points[i-1] 
            
            count+= max((abs(start_point[0]-points[i][0])),abs(start_point[1]-points[i][1]))
        return count
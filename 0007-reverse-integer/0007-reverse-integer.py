class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        num = 0
        if x < 0 :
              x = x*-1
              flag = 1
        while x >0 :
            num = (num*10) + (x%10)
            x = x//10
            
        if flag == 1 :
            num = num*-1
        if num < -2**31 or num > (2**31 - 1) :
            return 0
        else :
            return num
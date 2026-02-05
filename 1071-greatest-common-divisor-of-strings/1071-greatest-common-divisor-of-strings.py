class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1+str2 != str2+str1 :
            return ""
    
        l1,l2 = len(str1), len(str2)
        while l2 > 0 :
            l1, l2 = l2, l1 % l2
        return str1[:l1]
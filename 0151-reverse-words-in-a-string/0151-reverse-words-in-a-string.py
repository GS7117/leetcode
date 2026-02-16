class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = s.split()
    
        output = s[::-1]
        output = " ".join(output)
        return output
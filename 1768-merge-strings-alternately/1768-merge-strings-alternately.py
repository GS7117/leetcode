class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        newStr = ""
        for i in range (0, max(len(word1) , len(word2))) :
            if i  < min(len(word1),len(word2)) :
                newStr = newStr + word1[i] + word2[i]
            elif i < len(word1) :
                 newStr = newStr + word1[i]
            else :
                 newStr = newStr + word2[i]   
        return newStr
        
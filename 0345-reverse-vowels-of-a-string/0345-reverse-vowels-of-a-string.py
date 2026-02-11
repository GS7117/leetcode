class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aAeEiIoOuU")
        temp = list(s)
        i=0
        j=len(temp)-1
        while i<j :
            if temp[i] not in vowels :
                i+=1
            elif temp[j] not in vowels :
                j-=1
            else :
                temp[i] , temp[j] = temp[j], temp[i]
                j-=1
                i+=1
        return "".join(temp)
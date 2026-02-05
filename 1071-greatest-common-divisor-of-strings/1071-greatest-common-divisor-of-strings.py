class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        i=0
        l1 = len(str1)
        l2= len(str2)
        gcd =""
        final_gcd =""
        while i<l1 and i<l2 :
            if str1[i] == str2[i] :
                gcd = gcd + str1[i]
            
            if len(gcd) >0 and (gcd*(l1//len(gcd)) == str1 and gcd*(l2//len(gcd)) == str2)  :
                final_gcd = gcd
            i+=1
        return final_gcd
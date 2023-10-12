class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        t=""
        result=""
        if str1+str2!=str2+str1:
            return ""
        for i in range (min(len(str1),len(str2))):
            t+=str1[i]
            if(len(t)>0 and len(str1)%len(t)==0 and len(str2)%len(t)==0):
                result=t
        return result
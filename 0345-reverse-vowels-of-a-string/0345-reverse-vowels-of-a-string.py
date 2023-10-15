class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp=list(s)
        left=0
        right=len(s)-1
        vowels='aeiouAEIOU'
        while left<right:
            if temp[left] in vowels and temp[right] in vowels:
                temp[right],temp[left]=temp[left],temp[right]
                right-=1
                left+=1
            elif temp[left] not in vowels:
                left+=1
            elif temp[right] not in vowels:
                right-=1
        return ''.join(temp)
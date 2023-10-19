class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d={}
        ans=[]
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            ans.append(d[i])
        return sorted(ans)==sorted(set(ans))
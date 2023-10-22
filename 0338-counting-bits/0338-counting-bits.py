class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr=[0]
        for i in range (1,n+1):
            if i%2==0:
                arr.append(arr[i//2])
            else:
                arr.append(arr[i-1]+1)
        return arr
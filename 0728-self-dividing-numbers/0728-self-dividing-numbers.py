class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isself(n):
            temp=n
            while n:
                i=n%10
                if i==0 or temp%i!=0:
                    return False
                n=n/10
            return True
        thelist=[]
        for n in range(left,right+1):
            if isself(n):
                thelist.append(n)
        return thelist       
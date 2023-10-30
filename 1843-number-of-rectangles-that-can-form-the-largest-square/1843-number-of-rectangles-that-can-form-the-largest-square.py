class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        res=[]
        j=0
        for i in rectangles:
            m=min(i[0],i[1])
            res.append(m)
            j=max(j,m)
        return sum(1 for i in res if i>=j)
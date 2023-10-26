class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        n=len(names)
        people=[(names[i],heights[i]) for i in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                if people[i][1]<people[j][1]:
                    people[i],people[j]=people[j],people[i]
        ans=[person[0] for person in people]
        return ans
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        u=set()
        for i in nums:
            if i in u:
                u.remove(i)
            else:
                u.add(i)
        return u.pop()
            
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=[i for i in nums if (nums.count(i)==1)]
        return sum(nums)
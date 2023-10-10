class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        nums.reverse()
        i=0
        while i+2<len(nums):
            if nums[i]<nums[i+1]+nums[i+2] and nums[i]>nums[i+1]-nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
            else:
                nums.remove(nums[i])
        return 0
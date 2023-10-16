class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ind=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[i],nums[ind]=nums[ind],nums[i]
                ind+=1

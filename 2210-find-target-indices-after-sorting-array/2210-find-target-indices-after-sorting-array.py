class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    temp=nums[j]
                    nums[j]=nums[i]
                    nums[i]=temp
        for i in range(0,len(nums)):
            if(nums[i]==target):
                ans.append(i)
        return ans

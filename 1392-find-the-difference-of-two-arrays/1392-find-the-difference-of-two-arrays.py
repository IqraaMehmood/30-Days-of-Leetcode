class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        arr1=set(nums1)
        arr2=set(nums2)
        answer=[list(arr1-arr2),list(arr2-arr1)]
        return answer
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        marker=len(nums)+1
        for num in nums:
            index=abs(num)-1
            if nums[index]>0:
                nums[index]=-nums[index]
                
            else:
                a.append(abs(num))
               
        return a
            
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for num in nums:
            index=abs(num)-1
           
            if nums[index]<0:
                a.append(abs(num))
            else:
                nums[index]=-nums[index]
        return a
            
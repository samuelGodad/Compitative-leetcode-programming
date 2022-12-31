class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        array=[]

        for i in range(len(nums)):
            count=0
            for j  in range(len(nums)):
                if nums[i]>nums[j] and j!=i:
                    count+=1
            array.append(count)
        return array
                    


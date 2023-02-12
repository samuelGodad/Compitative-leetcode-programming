class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
       
        l = len(nums)
        k %=l
        while k!=0 and l!=1:
            i = -l
            for j in range(-k,0):
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
            l -= k
            k%=l

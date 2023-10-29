class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        min_len=float('inf')
        win_sum=0
        n=len(nums)
        for right in range(n):
            win_sum +=nums[right]
            while win_sum>=target:
                min_len=min(min_len,right-left+1)
                win_sum-=nums[left]
                left+=1
        if min_len !=float('inf'):
            return min_len
        else:
            return 0
        
                
                
            
        
                



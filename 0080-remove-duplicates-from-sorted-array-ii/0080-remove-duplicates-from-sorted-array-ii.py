class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n =len(nums)
        left=0
        right =0
        while right<n:
            count =1
            while right +1 < n and nums[right] ==nums[right+1]:
                right +=1
                count +=1
            for i in range(min(count,2)):
                nums[left] =nums[right]
                left+=1
                
            right+=1
        return left
            
        
        
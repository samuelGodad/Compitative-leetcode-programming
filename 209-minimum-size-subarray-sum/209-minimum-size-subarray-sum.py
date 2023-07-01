class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0
        n = len(nums)
        min_length =n+1
        sum = 0
        while right<n:
            sum += nums[right]
            while sum >= target:
                min_length = min(min_length, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1
        if min_length != n+1:
            return min_length
        return 0
    
   
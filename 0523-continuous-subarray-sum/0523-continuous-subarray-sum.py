class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    
  
        mod_dict = {0: -1}
        cumulative_sum = 0
        for i in range(len(nums)):
            cumulative_sum += nums[i]
            if k != 0:
                cumulative_sum %= k
            if cumulative_sum in mod_dict:
              
                if i - mod_dict[cumulative_sum] > 1:
                    return True
            else:
                mod_dict[cumulative_sum] = i
        return False
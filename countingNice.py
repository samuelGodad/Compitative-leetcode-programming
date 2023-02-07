# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

 class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
      
        n = len(nums)
        count = [0] * (n + 1)
        count[0] = 1
        odd_numbers = res = 0
        for i in range(n):
            if nums[i] % 2 == 1:
                odd_numbers += 1
            if odd_numbers >= k:
                res += count[odd_numbers - k]
            count[odd_numbers] += 1
        return res

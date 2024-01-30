class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        n = len(nums)
        right = 1
        while right < n:
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left

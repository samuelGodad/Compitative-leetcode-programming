# You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.

# Return the string that represents the kth largest integer in nums.

# Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.
def arr(nums,k):
    for i in range(len(nums)):
        mins=i
        for j in range(i+1,len(nums)):
            if int(nums[mins])<=int(nums[j]):
                mins=j
        (nums[mins],nums[i])=(nums[i],nums[mins])
    return nums[k-1]
k=3  
print(arr(["2","21","12","1"],k))

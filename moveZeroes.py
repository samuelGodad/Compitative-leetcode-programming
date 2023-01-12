# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
class Solution(object):
    def moveZeroes(self, arr):
      nonzero=[i for i in arr if i!=0]
      zeros = [j for j in arr if j==0]
      array=nonzero+zeros
      return array
arr = [0,1,0,3,12]
print(move(arr)) 

# second method
class Solution(object):
    def moveZeroes(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[count] = arr[i]
                count+=1
        while count < len(arr):
            arr[count] = 0
            count += 1
#  third method
def move(array):
    store=[]
    store0=[]

    for i in range(len(array)):
        if array[i]!=0:
            store.append(array[i])
        elif array[i]==0:
            store0.append(array[i])
    return store+store0

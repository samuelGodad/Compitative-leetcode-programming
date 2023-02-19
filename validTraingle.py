# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

# Example 1:

# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
class Solution(object):
    def triangleNumber(self,array):
        """
        :type nums: List[int]
        :rtype: int
        """
   
       
        answer=0

        array.sort()

        for i in range(2,len(array)):
            right=i-1
            left=0
            while right>left:
                if array[right]+array[left]>array[i]:
                    answer+=(right-left)
                    right-=1
                elif  array[right]+array[left]<= array[i]:
                    left+=1
        return answer

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

class Solution(object):
    import math
    def productExceptSelf(self, array):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(array)
        left_array=[0]*n
        right_array=[0]*n
        product=[0]*n
        left_array[0]=1
        right_array[n-1]=1
        if n==1:
            return 0
        
        
        for i in range(1,n):
            left_array[i]=array[i-1]*left_array[i-1]
        for j in range(n-2,-1,-1):
            right_array[j]=array[j+1]* right_array[j+1]
        for k in range(n):
            product[k]=left_array[k]* right_array[k]
        return product
   

        

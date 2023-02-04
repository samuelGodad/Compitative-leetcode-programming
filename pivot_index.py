# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.
class Solution(object):
    def pivotIndex(self, array):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        totale=sum(array)
        prefix_sum=0
        for i in range (len(array)):
            rs=totale- prefix_sum-array[i]
            if  prefix_sum==rs:
                return i
            prefix_sum+=array[i]
        return -1
    
        

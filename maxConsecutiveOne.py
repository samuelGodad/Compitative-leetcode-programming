class Solution(object):
    def longestOnes(self, A, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        end = 0
        zeros = 0
        max_len = 0
        while end < len(A):
            if A[end] == 0:
                zeros += 1
            while zeros > K:
                if A[start] == 0:
                    zeros -= 1
                start += 1
            max_len = max(max_len, end - start + 1)
            end += 1
        return max_len

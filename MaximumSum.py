class Solution(object):
    def maxSumTwoNoOverlap(self, A,L,M):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        for i in range(1, len(A)):
            A[i] += A[i-1]
        res, maxL, maxM = A[L+M-1], A[L-1], A[M-1]
        for i in range(L+M, len(A)):
            maxL = max(maxL, A[i-M] - A[i-L-M])
            maxM = max(maxM, A[i-L] - A[i-L-M])
            res = max(res, maxL + A[i] - A[i-M], maxM + A[i] - A[i-L])
        return res

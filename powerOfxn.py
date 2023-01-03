class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if x==0:
            return 0
        else:
            return x*self.myPow(x,n-1)

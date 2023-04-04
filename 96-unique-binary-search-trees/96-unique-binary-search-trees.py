class Solution:
    def numTrees(self, n: int) -> int:
        array = [0] * (n+1)
        array[0] = 1
        array[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                array[i] += array[j-1] * array[i-j]
        return array[n]

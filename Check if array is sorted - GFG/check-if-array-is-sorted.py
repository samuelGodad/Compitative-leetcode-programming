#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        pointer1=0
        pointer2=1
        while pointer2<n:
            if arr[pointer2]<arr[pointer1]:
                return False 
            pointer1+=1
            pointer2+=1
        return True 
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# } Driver Code Ends
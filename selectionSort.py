#User function Template for python3
# You dont need to read input or print anything. Complete the functions select() and selectionSort() ,where select() takes arr[] and starting point of unsorted array i as input parameters and returns the selected element for each iteration in selection sort, and selectionSort() takes the array and it's size and sorts the array.


# Expected Time Complexity: O(N2)
# Expected Auxiliary Space: O(1)

class Solution: 
    def select(self, arr, i):
        min_index = i
        n = len(arr)
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        return min_index

        # code here 
    
    def selectionSort(self, arr,n):
        
        for i in range(n):
        
            min_index = self.select(arr, i)
        
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
        return arr

        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends

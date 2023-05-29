class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
       
        array =[]
        for i in range(len(nums)):
            counter =0
            for j in range(len(nums)):
                if j!=i and nums[i]>nums[j]:
                    counter+=1
            array.append(counter)
        return array
    
        
                    
            
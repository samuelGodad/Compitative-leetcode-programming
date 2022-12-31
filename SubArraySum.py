class Solution(object):
    def subarraySum(self, nums, k):
       
        dictionary={0:1}
        summ=0
        counter=0
        for i in nums:
            summ+=i
            if summ-k in dictionary:
                counter+=dictionary[summ-k]
            if summ in dictionary:
                dictionary[summ]+=1
            else:
                dictionary[summ]=1
        return counter

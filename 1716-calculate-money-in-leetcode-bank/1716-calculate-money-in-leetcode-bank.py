class Solution:
    def totalMoney(self, n: int) -> int:
        result =0
        day =0
        deposit =1
        
        while day<n:
            result +=deposit
            day += 1
            deposit +=1
            if day % 7 ==0:
                deposit =1+ day //7 
        return result
            
                
        
            
    
            
        
        
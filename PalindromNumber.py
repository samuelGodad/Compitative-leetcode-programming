class Solution:
    def isPalindrome(self, number):
        reverse = 0
        temp = number

        while(temp > 0):
            Reminder = temp % 10
            reverse = (reverse * 10) + Reminder
            temp = temp //10
  
        if(number == reverse):
            return True
        else:
            return False

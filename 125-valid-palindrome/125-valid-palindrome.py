class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(char.lower()for char in s if char.isalnum())
        # for char in s :
        #     if char.isalnum():
        #         s=''.join(char)
        if s[::-1] ==s:
            return True
        else:
            return False
      
        
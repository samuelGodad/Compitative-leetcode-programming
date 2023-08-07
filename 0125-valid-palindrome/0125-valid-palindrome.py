class Solution:
    def isPalindrome(self, string: str) -> bool:
    #     s=''.join(char.lower()for char in s if char.isalnum())
    #     if s[::-1] ==s:
    #         return True
    #     else:
    #         return False
    # def isPalindrome(string):
        string =string.lower().strip().replace(" ","")
        reversed =''
        for i in string:
            if i.isalnum():
                reversed+=i

        return reversed[::-1]==reversed

        
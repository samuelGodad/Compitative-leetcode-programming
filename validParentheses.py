# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
   
        stack=[]
        for i in s:
            if i in ['(','[','{']:
               stack.append(i) 

            elif i== ']' and len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            elif i== ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            elif i== '}' and len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            else:
                return False

        return stack==[]

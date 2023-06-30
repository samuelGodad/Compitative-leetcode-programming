class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left_pointer=0
        right_pointer=0
        window_element= set()
        max_length=0
        while right_pointer <n:
            if s[right_pointer] not in window_element:
                window_element.add(s[right_pointer])
                right_pointer+=1
                max_length =max(max_length,right_pointer-left_pointer)
            else:
                window_element.remove(s[left_pointer])
                left_pointer+=1
        
        return max_length
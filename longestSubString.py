class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        dictionary={}
        substringLen=0
        start=0
        for i in range(len(s)):
            if s[i]in dictionary and start <=dictionary[s[i]]:
                start=dictionary[s[i]]+1
            else:
                substringLen=max(substringLen,i-start+1)
            dictionary[s[i]]=i
        return substringLen

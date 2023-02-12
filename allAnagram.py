class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        p_count = [0] * 26
        s_count = [0] * 26
        for i in range(len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1
        res = []
        for i in range(len(s) - len(p)):
            if p_count == s_count:
                res.append(i)
            s_count[ord(s[i]) - ord('a')] -= 1
            s_count[ord(s[i + len(p)]) - ord('a')] += 1
        if p_count == s_count:
            res.append(len(s) - len(p))
        return res

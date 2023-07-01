class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    # def characterReplacement(s, k):
        left = 0
        right = 0
        n = len(s)
        count = {}
        max_length = 0

        while right < n:
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(count.values())
            while right - left + 1 - max_count > k:
                count[s[left]] -= 1
                left += 1
                max_count = max(count.values())
            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length

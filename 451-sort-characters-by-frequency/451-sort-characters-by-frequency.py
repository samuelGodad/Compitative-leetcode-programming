class Solution:
    def frequencySort(self, s: str) -> str:
        no_char = {}
        for char in s:
            if char in no_char:
                no_char[char] += 1
            else:
                no_char[char] = 1
        sorted_chars = sorted(no_char.keys(), key=no_char.get, reverse=True)
   
        sorted_str = ""
        for char in sorted_chars:
            sorted_str += char *no_char[char]
        return sorted_str

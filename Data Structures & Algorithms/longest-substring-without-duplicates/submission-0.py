class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        i = 0
        j = 0

        while j < len(s):
            if s[j] not in s[i:j]:
                curr_l = j - i + 1
                max_l = max(curr_l, max_l)
                j += 1
            else:
                i += 1

        return max_l
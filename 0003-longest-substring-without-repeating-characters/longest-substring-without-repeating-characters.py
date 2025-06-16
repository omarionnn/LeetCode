class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        state = set()
        start = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in state:
                state.remove(s[start])
                start += 1

            state.add(s[r])
            longest = max(longest, r - start + 1)
        return longest
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=len(s)-1
        seen=set()
        max_len=0
        current_len=0

        for right in range(len(s)):

            while s[right] in seen:

                seen.remove(s[left])
                left+=1
            
            seen.add(s[right])
            current_len=(right-left)+1
            max_len=max(max_len,current_len)

        return max_len

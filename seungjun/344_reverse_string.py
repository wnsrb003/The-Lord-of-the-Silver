class Solution:
    def reverseString(self, s: List[str]) -> None:
        lt = 0
        rt = len(s) - 1
        
        while lt < rt:
            if s[lt] != s[rt]:
                s[lt], s[rt] = s[rt], s[lt]
            
            lt += 1
            rt -= 1

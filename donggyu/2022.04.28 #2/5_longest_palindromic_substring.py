s="babad"
#손코딩 까지는 완료했는데, 잘 구현되지 않아, 소스코드 참고
#
# s="a"
def longestPalindrome(self, s):
    res = ""
    for i in range(len(s)):
        # 홀수
        tmp = self.check(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # 짝수
        tmp = self.check(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res
 
# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
def check(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]









# #투포인터
# s = list(s)
# if len(s) == 1 or s == s[::-1]:
#     print(s)

# while True:

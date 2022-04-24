s = ["h","e","l","l","o"]
a = len(s)
for i in range(a//2) :
    s[i],s[a-i-1] = s[a-i-1],s[i]
print(s)
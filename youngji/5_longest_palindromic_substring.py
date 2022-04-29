
s = "cbbd"

s = list(s)
l = len(s)

maxi = 0
# for start in range(l) :
#     for end in range(l) :
#         words = s[start:end+1]
#         if words == words[::-1] :
#             if len(words) > maxi :
#                 result = words
#                 maxi = len(words)

# print(''.join(result))

start = 0
end = 2

if l == 1 :
    print(s)
if s[:2] == s[1::-1] : 
    result = s[:2]
    maxi = 2

while  1 :
    if start > l or end > l :
        break
    words = s[start:end+1]
    if words == words[::-1] :
        if len(words) >= maxi :
                result = words
                maxi = len(words)
                end += 1
    else : start += 1
    
print(''.join(result))
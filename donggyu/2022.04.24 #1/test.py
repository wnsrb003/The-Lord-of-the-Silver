import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

new_paragraph = re.sub('[^0-9a-zA-Z]', ' ',paragraph)
new_paragraph = new_paragraph.lower()
        
group = []
#단어 별로 묶기를 ... -> split() 사용
new = list(new_paragraph.split())
for i in new:
    a = new.count(i)
    b = i
    group.append([a, b])

for i in range(len(group)+1):
    if group[][i] == banned:

print(group)

#딕셔너리 공부해서 딕셔너리로 변경하기

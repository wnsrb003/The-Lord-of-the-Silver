import re
from collections import defaultdict,Counter

paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]

#sol.01 (준규형 풀이)
# arr = re.sub('[^0-9a-zA-Z]', ' ',paragraph)
# arr = list(arr.lower().split())
# graph = defaultdict(int)
# banned = list(map(lambda x: x.lower(), banned))
# # print(arr)
# for i in arr:
#     if not i in banned:
#         graph[i] += 1

# max = 0
# result = ''

# for k, v in graph.items():
#     if v > max:
#         max = v
#         result = k
# print(result)

#sol.02 (영지 풀이)
# banned = [ x.lower() for x in banned]
# paragraph = re.sub('[^0-9a-zA-Z]', ' ',paragraph)
# paragraph = list(paragraph.lower().split())
# paragraph = [i for i in paragraph if i not in banned]

# print(paragraph)
# cnt = Counter(paragraph)
# print(cnt.most_common(1)[0][0])

#sol.03 (미정누나 풀이)

arr = re.sub('[^0-9a-zA-Z]', ' ',paragraph)
arr = list(arr.lower().split())
ans = dict()
banned = list(map(lambda x: x.lower(), banned))
for word in arr:
    ans[word] = ans.get(word, 0)+1
max_key = max(ans, key=ans.get)
print(max_key)
# if max_key == banned[0]:
#     print()

#sol.04 (답지 풀이+)
words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()if word not in banned]

counts = Counter(words)
# 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
print(counts.most_common(1)[0][0]) 
import re
from collections import defaultdict
from unittest import result

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

arr = re.sub('[^0-9a-zA-Z]', ' ',paragraph)
arr = list(arr.split())
graph = defaultdict(int)
banned = list(map(lambda x: x.lower(), banned))

for i in arr:
    i = i.lower()
    if not i in banned:
        graph[i] += 1


max = 0
result = ''

for i, v in graph.items():
    if v > max:
        max = v
        result = i

print(result)
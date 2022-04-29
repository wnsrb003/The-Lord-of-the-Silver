strs = ["eat","tea","tan","ate","nat","bat"]
res_dict = dict()
res_list = list()

for str in strs:
    str_joined = ''.join(sorted(str))
    
    if str_joined not in res_dict.keys():
        res_dict[str_joined] = list()
        
    res_dict[str_joined].append(str)
    
for value in res_dict.values():
    res_list.append(value)
    
print(res_list)
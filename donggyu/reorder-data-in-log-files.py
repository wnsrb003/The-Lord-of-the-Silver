class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
   
        for log in logs:
            if log.split()[1].isdigit(): #숫자가 포함된 log는 [1]부터 있음 // 어려웠음
                digits.append(log)
            else:
                letters.append(log) #그외(문자로만 구성된(식별자 제외) 로그는 letter 리스트에 추가)
        letters.sort(key=lambda x:(x.split()[1:], x.split()[0])) #말도안됨
        return letters+digits

#문자로 구성된 로그가 우선
    #같은 로그이면 식별자 우선순위 [lamda식 사용하자]
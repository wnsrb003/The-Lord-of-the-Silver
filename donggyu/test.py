s = ['2a', '1b', '4c', '1a']

    #함수식
def func(x):
    return x.split()[1], x.split()[0]
    
print(s.sort(key=func))

    #람다식
# s.sort(key=lambda x: (x.split()[1], x.split()[0]))
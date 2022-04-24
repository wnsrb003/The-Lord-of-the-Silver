from curses.ascii import isalpha


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

# logs = [list(i.split()) for i in logs]
a = []
for i in logs :
    if i.split()[1].isalpha() :
        a.append(i)
a.sort(key=lambda x : (x.split()[1:],x.split()[0]))
print(a)
for i in logs :
    if i.split()[1].isalpha() == False :
        a.append(i)

import re
with open('hamlet.txt') as file:
    words=[]
    for line in file:
        re.sub(r'[^\w\s]', '',line)
        line=line.strip().replace('.','')
        words+=line.split()
    print(words)
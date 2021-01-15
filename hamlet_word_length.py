import re
with open('hamlet.txt') as file:
    words=[]
    for line in file:
        re.sub(r'[^\w\s]', '',line)
        line.strip()
        words+=line.split()
    total=0
    for word in words:
        total+=len(word)
    avg_length=total/len(words)
    print(f'The average word length of "Hamlet" is {avg_length}.')


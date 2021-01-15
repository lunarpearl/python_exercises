import re
with open('jenseits_von_gut_und_boese.txt') as file:
    words=[]
    for line in file:
        re.sub(r'[^\w\s]', '',line)
        line.strip()
        words+=line.split()
    total=0
    for word in words:
        total+=len(word)
    avg_length=total/len(words)
    print(f'The average word length of "Jenseits von Gut und Boese(Beyond Good and Evil)" is {avg_length}.')


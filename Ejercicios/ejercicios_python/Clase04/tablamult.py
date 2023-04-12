# tablamult.py
blank=''
header=f'{blank:>4}'
separator=f'{blank:->4}'
rows=[]
for n in range(10):
    header+=f'{n:4d}'
    separator+=f'{blank:->4}'
    row=f'{n}:  '
    j=0
    for m in range(10):
        row+=f'{j:>4d}'
        j+=n
    rows.append(row)

rows = [header, separator]+ rows
for r in rows:
    print(r)
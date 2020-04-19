#!/usr/bin/python3
def GetText():
    tex=open("/root/aaa.txt","r").read()
    tex=tex.lower()
    for ch in '|"#$%&()*+,./:;<=>?@[\\]^_{|}~':
        tex = tex.replace(ch," ")
    return tex
#print(GetText())
hatext = GetText()
words = hatext.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0)+1
items = list(counts.items())
print(len(items))
print(items)
items.sort(key=lambda x:x[1],reverse=True)

for i in range(len(items)):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))

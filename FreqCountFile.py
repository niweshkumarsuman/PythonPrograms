fp=open("abc.txt",mode='rt')
dict1={}
for line in fp.readlines():
    for word in line.split():
        for char in word:
            if(char in dict1.keys()):
                dict1[char]+=1
            else:
                dict1[char]=1
print(dict1)
str = "Success"
str = str.lower()
char = []
for i in str:
    if str.count(i,0,len(str)) > 1:
        str = str.replace(i,'1')
    else:
        str = str.replace(i,'2')

result = str.replace('1',')')
result = result.replace('2','(')
print(str)
print(result)

def duplicate_encode(word):
    return "".join("(" if word.lower().count(c) == 1 else ")" for c in word.lower())
word = 'werasdfa'
print(duplicate_encode(word))
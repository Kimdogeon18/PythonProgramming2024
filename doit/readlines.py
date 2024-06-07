# readlines.py

f = open('새파일.txt', 'r')
lines = f.readlines()
print(type(lines))
for line in lines:
    print(line)
f.close()

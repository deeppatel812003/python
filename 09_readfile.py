f = open('sample.txt', 'r')
data = f.read()
print(data)
data = f.readline() # readline
print(data)
data = f.readline()
print(data)
f.close()
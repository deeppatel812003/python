with open('sample.txt','r')as f:
    a = f.read()
print(a)

with open('new.txt','w')as f:
    b = f.write("deep patel")
print(b)

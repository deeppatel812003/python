def remove_and_split(string,word):
    newstr = string.replace(word,"")
    return newstr.strip()

this = " i am fine"
n = remove_and_split(this,"fine")
print(n)

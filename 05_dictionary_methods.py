mydict = {
    "fast" : "In a quick manner",
    "marks": "[7,4,,8]",
    1:2
    
}
print(mydict)
#prints the keys of dictionary
print(list(mydict.keys()))
#values of dictionary
print(list(mydict.values()))
#items
print(list(mydict.items()))
#update
print(mydict)
updatedict={
"deep":"friend"
}
mydict.update(updatedict)
print(mydict)
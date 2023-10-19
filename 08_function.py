def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return p
marks = [87,93,65,43]
percentage = percent(marks)
print(percentage)
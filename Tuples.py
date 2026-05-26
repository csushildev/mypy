#Immutable's of python

year1marks=(85, 92, 78, 92, 96, 88,92)
print(year1marks[0])
print(year1marks[1:3])
yearsubsetmarks = year1marks[1:4]
print(yearsubsetmarks)

#get the last index of 92 in tuple
print(year1marks.index(92,4))
print(year1marks.index(92,4))
#print(year1marks.index(92,7))   error as there is no 92 after index 6

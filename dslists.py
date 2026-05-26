#matrics can be created using python lists#

marks = [85, 92, 78, 96, 88, "test",["Sushil",11025,"class5"]]

print(marks[6][1])
print(marks[1:3])

str = "sushil"
#str[0]="S"

marks[1] = 95
print(marks)

#adding an element 1 at the start of the list, 2 at the end of the list and 3 at index 2
marks.insert(0,1)
marks.append(2)
marks.insert(2,3)
marks.insert(13,10)
print(marks.__len__(),marks)

#list comprehension

table = [5*i for i in range(1,11)]
print(table)

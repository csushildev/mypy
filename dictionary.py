'''dictionary and methods examples'''

marks = {'maths': 90, 'english': 80, 'science': 85}
print(marks['maths'])
print(marks.get('english')) 
print(marks.get('history', 'not found')) #if key is not found it will return 'not found' instead of error
marks['history'] = 75 #to add a new key-value pair to the dictionary
print(marks)
marks['maths'] = 95 #to update the value of an existing key
print(marks.keys()) #to get all the keys in the dictionary


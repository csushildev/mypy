#Lambdas - ANONYMous Functions 
# looks like declare expression in pega. "whenever used "

x = (lambda a,b:a*b)(85,2)

print(x)

lst = [54,45,23,47,34]
print(lst)
# Apply filter on the list of elements and save it to another list.
newlst1=list(filter(lambda x:x>40,lst))
print(newlst1)

#use of map funtion with lambda3+3
newlst2=list(map(lambda y:y*2,lst))
print(newlst2)

#user of range function
newlst3=list(filter(lambda x:x>40,list(range(35,45))))
print(newlst3)

price = 12.99
quantity = 2

print(f"The total cost is ${price:.2f} x {quantity} = ${price * quantity}.")

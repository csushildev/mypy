#Assignment 1 : 

print('Hello \"SIR\" \u2764 ')

def factors_and_classification(number):
    factors = []
    
    # Find the factors of the given number
    for r in range(1, number + 1):
        if number % r == 0:
            factors.append(r)
    
    # Check whether each factor is even or odd
    factor_classification = {}
    for factor in factors:
        if factor % 2 == 0:
            factor_classification[factor] = 'Even'
        else:
            factor_classification[factor] = 'Odd'
    
    return factors, factor_classification

# Input a number
number = int(input("Enter number to get factor: "))

factors, factor_classification = factors_and_classification(number)

# Display the factors and their classifications
print(f"Factors of {number}: {factors}")
for factor, classification in factor_classification.items():
    print(f"{factor} is {classification}")
	


#Assignment 2
# Input CSV 
SeqOfWords = str(input("Enter the sequence of words seperated with comma(,) : "))

ListOfWords = SeqOfWords.split(',')

print(ListOfWords)





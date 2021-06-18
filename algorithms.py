#PRACTICE WITH ALGORITHIMS

# ## 1. Bubble Sort
# Write a program to sort a list of numbers in ascending order, comparing and swapping two numbers at a time.
# ```python
# [3,1,4,2]
# [1,3,4,2]
# [1,3,2,4]
# [1,2,3,4]
# ```
input = [3,1,4,2,22,13,49,5,15]
def BubbleSort(input):
    n = len(input)
    
    hasSwapped = False
    for i in range(n-1):
        if (input[i] > input[i+1]):
            holder = input[i]
            input[i] = input[i+1]
            input[i+1] = holder
            hasSwapped = True

    print(input)

    if(hasSwapped == True):
        BubbleSort(input)


BubbleSort(input)

print("------------------------------------------------")

# ## 2. Candies
# Given the list `candies` and the integer `extra_candies`, where `candies[i]` represents the number of candies that the `ith` kid has.
# For each kid, check if there is a way to distribute the `extra_candies` amount to the kids such that they can have the greatest numhber of candies among them. Notice that multiple kids can have the greatest number of candies.
# ```python
# candies = [2,3,5,1,3]
# extra_candies = 3
# expected output: [True,True,True,False,True]
# ```
candies = [2,3,5,1,3]
extra_candies = 3

def Candies(input, x):
    output_buffer = []
    print(input)
    for i in input:
        if(i + x >= max(input)):
            output_buffer.append(True)
        else:
            output_buffer.append(False)
    print(output_buffer)

Candies(candies, extra_candies)

print("------------------------------------------------")
# ## 3. Shuffle
# Given a string `s` and an integer list of `indices` of the same length, shuffle the string such that the character at the `ith` position moves to `incices[i]`.
# Return the shuffled string.
# ```python
# s = "odce"
# indices = [1,2,0,3]
# return "code"
# ```
s = "odce"
indices = [1,2,0,3]
def Unshuffle(string, indices):
    print(indices)
    print(string)
    n = len(indices)
    returnString = ""
    for i in range(n):
        for j in range(n):
            if indices[j] == i:
                returnString = returnString + string[j]
    
    return returnString
        
print(Unshuffle(s, indices))

# ## 4. Primes
# Write a program that returns a list of all prime numbers up to a given max(inclusive).
# A prime is a number that only has two factors; itself and 1.
# ```python
# n=12
# [2,3,5,7,11]
# ```

max = 12
def PrimesToMax(input):
    print(input)
    primes = []
    for i in range(1,input):
        isPrime = True
        for j in range(i+1, input):
            if(i % j == 1):
                isPrime = True
            else:
                isPrime = False
        if(isPrime == True):
            primes.append(i)

    print(primes)

PrimesToMax(max)
        
                


# ## 5. FizzBuzz
# A classic; write a program that prints out a sequential string of numbers.
# If divisible by 3, output `"Fizz`.
# If divisible by 5, output `"Buzz`.
# If divisible by both 3 and 5, output `FizzBuzz`.
# Otherwise, print out the string.
# ```python
# Between 1 and 5, output:
# "1"
# "2"
# "Fizz"
# "4"
# "Buzz"
# ```
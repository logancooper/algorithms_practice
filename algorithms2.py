
# 1. Reverse a string
# Given a string of letters, return the reverse of that string. Complete this without using any special built in methods.

def ReverseString(string):
    returnString = ""
    
    #For every letter in the string
    for i in range(len(string)):
        #From the back append each letter to the return string
        #print(i)
        #print(((len(string) - (i + 1))))
        returnString = returnString + string[((len(string) - (i + 1)))]
        
    #Return
    return returnString
 
# 2. Remove Duplicates
# Given a string of letters and / or numbers, remove all duplicates and return the new string. Study the example carefully. Please avoid any special built in methods or operators (Set).

def RemoveDuplicates(string):
    #for each of the letters in string
    for i in range(len(string)):
        #look at each letter of the string
        for j in range(len(string)):
            #if you're not at the same index and the characters are the same, remove the character from the string
            if(i != j and string[i] == string[j]):
                string.replace(string[j],"")

    return string

# 3. Is this an Anagram?
# Given two strings, check if they are anagrams, and return a boolean.

def IsAnagram(string1, string2):
    
    #If both strings contain the same number of characters
    if(len(string1) == len(string2)):
        #for each letter in string 1
        for i in range(len(string1)):
            #look at each letter in string 2
            for j in range(len(string1)):
                #if the letters match
                if string1[i] == string2[j]:
                    #???
                    return string1
    return string1
    #return isAnagram

#Main Program
inputString = "Hello DigitalCrafts"

print(ReverseString(inputString))
#print(RemoveDuplicates(inputString))
#print(IsAnagram(inputString))
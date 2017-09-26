##"""Write a program that outputs all possibilities to put + or - or nothing
##between the numbers 1,2,…,9 (in this order)such that the result is 100.
##For example 1 + 2 + 3 - 4 + 5 + 6 + 78 + 9 = 100."""
##import numpy as np
##a = 100
##while a <= 100:
##    a = 

"""Write function that translates a text to Pig Latin and back. English
is translated to Pig Latin by taking the first letter of every word, moving
it to the end of the word and adding ‘ay’. “The quick brown fox” becomes
“Hetay uickqay rownbay oxfay”."""
def PigLatin():
    a = input('')
    for t in a:
        spaced = a.find(' ')
        if t == spaced + 1:
            spaced = 'ay '
        else:
            spaced = ' '
    return a
print(PigLatin())



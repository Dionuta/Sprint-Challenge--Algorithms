'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
     
    sub_word="th"
    # if the word length is zero return 0
    if len(word) == 0: 
        return 0

    # starts the at the beginning of word check if subword is at the start
    # if so count goes up then we move a space over 

    elif word[0 : len(sub_word)] == sub_word: 
        return 1 + count_th(word[1:]) 

    # keep checking till base case is reached 
    return count_th(word[1:])
    
print(count_th("mjthsxth"))
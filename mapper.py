def letterToIndex(letter):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    idx = alphabet. find(letter)
    if idx == -1:   #means that wasn't in the alphabet
        print("error:", letter, "is not in the alaphabet")
    return idx

def indexToLetter(idx):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    letter = ''
    if idx >= len(alphabet):
        print("error:", idx, "is to large")
    elif idx < 0:
        print("error:", idx, "is to small")
    else:
        letter = alphabet[idx]
    return letter

#this is a secret message that i want to translate
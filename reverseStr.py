#Three different ways to reverse a string in Python


#1

def reverse_string1(s):
    return " ".join(reversed(s.split()))

#2
def reverse_string2(s):
    return " ".join(s.split()[::-1])

#3 - manual


def reverse_string3(s):
    words = []
    length = len(s)
    space = [' ']

    i = 0

    while i < length:
        if s[i] not in space:
            word_start = i

            while i < length and s[i] not in space:
                i += 1

            words.append(s[word_start:i])
        i += 1
    return " ".join(reversed(words))




               

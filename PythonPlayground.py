import random
# 7

napis = "Gory sa fajnEe Y y"

def reverse(string):
    output = []
    for i in range(0, len(string)):
        output.append(string[(len(string) - 1) - i])
    return "".join(output)

# 8

def if_vowel(text, ind):
    vowels = ["a", "A", "i", "I", "u", "U", "o", "O", "e", "E"]
    for i in range(0, len(vowels)):
        if text[ind] == vowels[i]:
            return vowels[i]

def anti_vowel(text):

    textlist = []
    vowlist = []
    for i in range(0, len(text)):
        textlist.append(text[i])

    for i in range(0, len(textlist)):
        if if_vowel(textlist, i) != None:
            vowlist.append(if_vowel(textlist, i))

    for i in range(0, len(vowlist)):
        textlist.remove(vowlist[i])

    return "".join(textlist)


# 9 SCRABBLE

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

word = "Prokrastynacjazz"

def scrabble_score(word):
    punkty = 0
    word = word.lower()
    for i in range(0, len(word)):
        score.has_key(word[i])
        punkty = punkty + score[word[i]]
    return punkty

# 10 CENSOR

text = "I count slowly count lalalala, count basd count"
word = "count"

def censor(text, word):
    textlist =[]
    for i in range(0, len(text)):
        textlist.append(text[i])
    while text.find(word,0 ,len(text)) != -1:
        for i in range(0, len(word)):
            print text[text.find(word,0 ,len(text)) + i]
            textlist[text.find(word,0 ,len(text)) + i] = "*"
        text = "".join(textlist)
    return text

# print censor(text, word)

# 11 count

el_list = ["a", "b", "c", "a", "x", "d", "a", "a", "l", "a", "a"]
key = "a"


def count(sequence, item):
    counter = 0
    for i in range(0, len(sequence)):
        if item == sequence[i]:
            counter = counter + 1
    return counter

# print count(el_list, key)

# 12 Purifier

numbers = []
for i in range(0, 7):
    numbers.append(random.randrange(0, 20, 1))

print numbers

def purify(numlist):
    output =[]
    for i in range (0, len(numlist)):
        if numlist[i] % 2 == 0:
            output.append(numlist[i])
    return output

print ""
# print purify(numbers)

# 13 Product

def product(numlist):
    output = 1
    for i in range (0, len(numlist)):
        output = output * numlist[i]
    return output

# print product(numbers)

# 15 Median

def median(numlist):
    if len(numlist) % 2 == 0:
        print "median even"
        return median_even(numlist)
    else:
        print "median uneven"
        return median_uneven(numlist)

def sortlist(numlist):
    list_sorted = []
    for i in range(0, len(numlist)):
        list_sorted.append(min(numlist))
        numlist.remove(min(numlist))
    return list_sorted

def median_uneven(numlist):
    list_sorted = sortlist(numlist)
    print list_sorted
    return list_sorted[len(list_sorted) / 2]

def median_even(numlist):
    list_sorted = sortlist(numlist)
    median_avg = (list_sorted[len(list_sorted) / 2] + list_sorted[(len(list_sorted) / 2) - 1]) / 2.0
    print list_sorted
    return median_avg

print median(numbers)

import random

print()
print ("Welcome to the Daily Wordle Solver by Mangalik Mitra")
print ()
print ("Please enter your first word (suggestions: ORATE, ADIEU, ARISE, ROATE):", end = " ")
word = input().lower()

possible_letters = [] 
abet = list(map(chr, range(97, 123)))
dic = {}
for thinf in abet:
    dic[thinf] = 0
for i in range(5):
    possible_letters.append(list(map(chr, range(97, 123))))

word_list = [] #stores many 5-letter words brought in from sgb-words.txt

f = open("bad_words.txt", "r")
for toke in f:
    if len(toke) == 6:
        word_list.append(toke)
f.close()

print ("Please enter the result after the first word (x for grey, g for green, and y for yellow for each of the 5 positions): ", end = "")
result = input()

corr_ind = 0
answers = ["Genius", "Magnificent", "Impressive", "Splendid", "Great", "Phew"]

already_green = []
tobechecked = []
for count in range(5):

    if result == "ggggg":
        break
    corr_ind = corr_ind + 1
    for indes in range(5):
        if result[indes] == "g":
            possible_letters[indes] = [word[indes]]
            if indes not in already_green:
                already_green.append(indes)
        elif result[indes] == "x":
            for k in range(5):
                if word[indes] in possible_letters[k] and len(possible_letters[k]) != 1:
                    possible_letters[k].remove(word[indes])
        elif result[indes] == "y":
            possible_letters[indes].remove(word[indes])
            dic[word[indes]] = dic[word[indes]] + 1
            if word[indes] not in tobechecked:
                tobechecked.append(word[indes])
    toberemoved = []
    for s in range(len(word_list)):
        keep_checker = 1
        shobdo = word_list[s]
        for hj in range(5):
            if shobdo[hj] not in possible_letters[hj]:
                keep_checker = 0
                break
        for thing in tobechecked:
            counte = 0
            for hj in range(5):
                if hj in already_green:
                    continue
                if shobdo[hj] == thing:
                    counte = counte + 1
            if counte < dic[thing]:
                keep_checker = 0
                break            
        if keep_checker == 0:
            toberemoved.append(word_list[s])
    for thinf in abet:
        dic[thinf] = 0
    tobechecked = []
    
    for theones in toberemoved:
        word_list.remove(theones)

    print()
    print("Try this word: ", end = "")
    #print(word_list[random.randint(0, len(word_list)-1)], end = "")
    random.shuffle(word_list)
    jg = 0
    want = "yes"
    while want == "yes":
        if (jg > 0):
            print("Try this word: ", end = "")
        print(word_list[jg], end = "")
        jg = jg + 1
        if (jg >= len(word_list)):
            jg = 0
        print ("Do you want another suggestion?", end = " ")
        want = input()
        
        
    
    print("\nWhich word did you enter this time?", end = " ")
    word = input().lower()
    print ("Please enter the result after the word (x for grey, g for green, and y for yellow for each of the 5 positions): ", end = "")
    result = input()

if result == "ggggg":
    print ("\n" + answers[corr_ind])
else:
    print ("\nHard luck!")
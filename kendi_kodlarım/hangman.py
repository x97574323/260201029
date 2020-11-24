import random
words=["know","water" ,"than" ,"call","first","who","may","down","side","been","now","find","any"]
word=words[random.randint(0, len(words)-1)]
length=len(word)
counter=[]
chance=5
while(True):
    if chance>0:
        if(len(counter)==length):
            print("Congrats You Won!! word is {}".format(word))
            break 
        returner=""
        for k in word:
            if(word.index(k) in counter):
                returner=returner+k
            else:
                if(len(returner)<length):
                    returner=returner+"-"
        print("Word is {}".format(returner))
        word_input=input("Input your guess:")
        if(word_input in word):
            for i in word:
                if(word_input==i):
                    index=word.index(i)
                    counter.append(index)
            print("Congralations your chracter in the word!")
            print("you have {} chances".format(chance))
        else:
            chance=chance-1
            print("Wrong chracter!! you have {} chances".format(chance))
    else:
        print("You lost there is no chance word was {}".format(word))
        break
    
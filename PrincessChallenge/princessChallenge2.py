#!/usr/bin/env python3


## create questionBank object and get data from question.txt 
qBank = open("qustion.txt", "r")
qList = qBank.read().splitlines()
qBank.close()

## merge the list to get actual questionbank
def mergeQuestion(list) :
    i = 0
    j = 0 
    retList = []
    while i < len(list):
        retList.append(list[i].strip() + "\n" + list[i+1].strip() + "\n\n")
        i += 2
        j += 1
    return retList
qustionbank = mergeQuestion(qList)

## ask question and try to get an answer: 
def askQuestion(question, s):
    answer = input(question)
    if answer.upper() == "A":
        s = s + "A"
        return s
    elif answer.upper() == "B":
        s = s + "B"
        return s
    elif answer == "QUIT":
        print("Bye, maybe next time you could be a real princess")
        exit()
    else:
        print("\n!!!!!\nPlease choose from A or B. if you don't want to play anymore, please enter QUIT to exit.\n\n")    
        askQuestion(question, s)

startGame = input("****************************************************\n would you like to know which Princess you are? please enter YES to play or any key to exit \n****************************************************\n")if startGame.upper() != "YES":
    print("sorry to hear that. please run princessChallenge.py whenever you would like to play")  
else: 
    print("\n\n\nPlease Be Honest to following question and choose your Answer of either A or B. if you would like to quit the game at anytime, please enter QUIT to exit\n\n\n")
    firstAnswer = askQuestion(qustionbank[0], "")
    if firstAnswer == "A": # go to question 1
        secondAnswer = askQuestion(qustionbank[1],firstAnswer)
    else: # go to question 2
        secondAnswer = askQuestion(qustionbank[2], firstAnswer)
    if secondAnswer == "AA": # go to question 3
        thirdAnswer = askQuestion(qustionbank[3],secondAnswer)
    elif secondAnswer == "AB" or "BA": # go to question 4
        thirdAnswer = askQuestion(qustionbank[4],secondAnswer)
    elif secondAnswer == "BB": # go to question 5
        princess = askQuestion(qustionbank[5],"")
        if princess == "A":
            print("Rapunzel")
            exit()
        else: 
            print ("Ariel")
            exit()
    if thirdAnswer == "AAA": # go to question 6
        princess = askQuestion(qustionbank[6],"")
        if princess == "A":
            print("Aurora")
            exit()
        else: 
            print ("Jasmine")
            exit()
    elif thirdAnswer == "AAB":
        fouthAnswer = askQuestion(qustionbank[4],thirdAnswer)
    elif thirdAnswer == "ABA" or "BAA":
        princess = askQuestion(qustionbank[7],"")
        if princess == "A":
            print("Snow White")
            exit()
        else: 
            print ("Belle")
            exit()
    else: #thirdAnswer == "ABB" or "BAB"
        princess = askQuestion(qustionbank[8],"")
        if princess == "A":
            print("Mulan")
            exit()
        else: 
            print ("Cinderella")
            exit()
    if fouthAnswer == "AABA":
        princess = askQuestion(qustionbank[7],"")
        if princess == "A":
            print("Snow White")
            exit()
        else: 
            print ("Belle")
            exit()
    else:
        princess = askQuestion(qustionbank[8],"")
        if princess == "A":
            print("Mulan")
            exit()
        else: 
            print ("Cinderella")
            exit()


    



    
    
    
    




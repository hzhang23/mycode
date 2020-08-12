#!/usr/bin/env python

#add question bank for princess test
questionBank = [
"1. favorite weekend activities: \n A: walk in the woods      B:alone time        C: hanging with friends",

"2. The animal that will lead your royal parade is : \n A:fish        B: dragon         C: raccoon",

"3. The most important quality you look for in a price is: \n A:charm        B: Kindness     C: humor",

"4. which one of these outfit elements are you most likely to wear? \n A: Vest       B: Dress        C:Sweats",

"5. favorite place to burst into song is: \n A:shower         B: anytime      C: I don’t sing",

"6. your favorite hair style is: \n A: bangs     B: stylish bob         C: ponytail",

"7. someday you want to be: \n A: singer       B:CEO         C:Baker",

"8. in one word, your style is: \n A: Fun      B: Classic      C: Colorful",

"9. you live in a : \n A: Castle       B: Big City     C:Small town",

"10. it is 4:00 pm! That’s means it’s time to: \n A: hit the gym      B:take a nap        C:have a snack",

"11. what is your favorite color: \n A:Blue      B:Yellow        C:RED"
]
#return result based on score
def returnResult(x):
    base = len(questionBank)*3
    if x/base < 0.5:
        print("******************************* \n you are Ariel! \n*******************************")
    elif x/base > 0.75:
        print("******************************* \n you are Snow White! \n*******************************")
    else:
        print("******************************* \n you are Cinderalla! \n*******************************")
#interact with user
score = 0
i = 0
startGame = input("****************************************************\n would you like to know which Princess you are? please enter YES to play or any key to exit \n****************************************************\n")
if startGame.upper() != "YES":
    print("sorry to hear that. please run princessChallenge.py whenever you would like to play")
else:
    while i < len(questionBank):
        answer = input(questionBank[i]+ "\n")
        if answer.upper() == "A":
            score = score + 1
            i += 1
        elif answer.upper() == "B":
            score = score + 2
            i += 1
        elif answer.upper() == "C":
            score = score +3
            i += 1
        else:
            print("Please choose from A , B or C")

    returnResult(score)

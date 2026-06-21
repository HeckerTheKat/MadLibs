import time as t
import sys as s

def prompt(type):
            print("Enter " + type + ".")
            word = input()
            words.append(word)
words = []
while True:
    num = input("Enter a whole number from 1 to 3. (Or type 0 to quit)\n")
    try:
        num = int(num)
    except ValueError:
        print("That's not a whole number.")
        t.sleep(1)
        continue
    if num == 0:
        print("This program will close in 5 seconds!")
        for i in range(5, 0, -1):
            print(i)
            t.sleep(1)
        s.exit()
    elif num < 1 or num > 3:
        print("That number isn't a number from 1 to 3.")
        t.sleep(1)
    elif num == 1:
        prompt("an animal")
        prompt("a game or a sport")
        prompt("\"good\" or \"bad\"")
        prompt("a place")
        prompt("a food")
        prompt("a drink")
        prompt("a plural noun")
        prompt("a plural noun")
        prompt("a plural noun")
        print("loading paragraph...")
        t.sleep(3)
        print("One time there was a", words[0], "that played", words[1], "and was really", words[2], "at it.\nThen, one day, he went to", words[3] + ".\nHe ate some", words[4], "and drank some", words[5] + ".\nThen, he realized that it wasn't about if he was good or bad at", words[1], ".\nIt was about the", words[6] + ".\nNot the", words[7], "or the", words[8] + ".\nIt was about the", words[6] + ".")
    elif num == 2:
        prompt("an animal")
        prompt("a drink")
        prompt("a fruit (must be plural noun)")
        prompt('"man" or "woman"')
        prompt("a place, use article if common noun")
        prompt("a singular noun")
        print("loading paragraph...")
        t.sleep(3)
        print("A", words[0], "walked up to a", words[1], "stand. The", words[0], "said \"Got any", words[2] + "? The", words[3], 'said "Nuh - Nope." So the', words[0], "went to the", words[4], "and tried to convince the manager to give him a free", words[5], "pass. They said yes, and the", words[0], "lived happily ever after.")
    elif num == 3:
        prompt("an animal")
        prompt("a store (proper noun)")
        prompt("a plural noun")
        prompt("a plural noun")
        prompt("a plural noun")
        prompt("a singular noun")
        prompt("a number")
        prompt("a company or brand")
        prompt("a plural noun")
        prompt('"yes" or "no"')
        print('One time, a', words[0], 'went to', words[1] + '. They bought', words[2] + ',', words[3] + ',', 'and a lot of', words[4] + '. When they went to the checkout, their', words[5], 'had a sum of', words[6], 'dollars. They tried swiping their', words[7], 'debit card and it didn\'t work. They tried swiping again. It still didn\'t work. So they put all their', words[8], 'back and went to the bank and asked for a credit card that he\'d payoff in a few years. They said', words[9] + '. The End.')
    t.sleep(20)
    words.clear()

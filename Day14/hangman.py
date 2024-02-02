import random

words =["UMRELLA","COMPUTER","TELESCOPE","SMARTPHONE"]
word = random.choice(words)

total_chances= 7
guessed_word = "-"*len(word)

print(guessed_word)
letter = input("Guess a letter:").upper()
if letter in word:
    for index in range(len(word)):
        if word[index]==letter:
            guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]
            print(guessed_word)  

    if guessed_word == word:
       print ("Congratulation you won!!!")
       break 

else:
    total_chances -= 1
    print("Incorect guess") 
    print("The remaining changes are:",total_chances)

print("Game over")
print("You Lose")
print("All the changes are exhasted")

print("The correct word is",word)


       

import random
from tkinter import *
from tkinter import messagebox

run = True
score = 0

def check(letter, button):
    global count, win_count, score, run
    exec('{}.destroy()'.format(button))
    if letter in word:
        for i in range(0, len(word)):
            if word[i] == letter:
                win_count += 1
                exec('d{}.config(text="{}")'.format(i, letter.upper()))
        if win_count == len(word):
            score += 1
            answer = messagebox.askyesno('GAME OVER', 'YOU WON!\nDO WANT TO PLAY AGAIN?')
            if answer:
                run = True
                root.destroy()
            else:
                run = False
                root.destroy()
    else:
        count += 1
        exec('c{}.destroy()'.format(count))
        exec('c{}.place(x={},y={})'.format(count + 1, 300, -50))
        if count == 6:
            answer = messagebox.askyesno('GAME OVER', 'YOU LOST!\nDO WANT TO PLAY AGAIN?')
            if answer:
                run = True
                score = 0
                root.destroy()
            else:
                run = False
                root.destroy()

root = Tk()
root.geometry('905x700')
root.title('HANGMAN BY PYTHONGEEKS')
root.config(bg='#ffffe7')
count = 0
win_count = 0

words = ['programming', 'data', 'python', 'code', 'computer', 'engineer', 'word', 'science', 'machine', 'java', 'college', 'player', 'mobile', 'image']
word = random.choice(words)

x = 250
for i in range(0, len(word)):
    x += 60
    exec('d{}=Label(root, text="_", bg="#ffffe7", font=("arial", 40))'.format(i))
    exec('d{}.place(x={},y={})'.format(i, x, 450))

icon = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for let in icon:
    exec('{}=PhotoImage(file="{}.png")'.format(let, let))

hangman_img = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7']
for hangman in hangman_img:
    exec('{}=PhotoImage(file="{}.png")'.format(hangman, hangman))

Button = [['btn1', 'a', 0, 595], ['btn2', 'b', 70, 595], ['btn3', 'c', 140, 595], ['btn4', 'd', 210, 595], ['btn5', 'e', 280, 595],
          ['btn6', 'f', 350, 595], ['btn7', 'g', 420, 595], ['btn8', 'h', 490, 595], ['btn9', 'i', 560, 595], ['btn10', 'j', 630, 595],
          ['btn11', 'k', 700, 595], ['btn12', 'l', 770, 595], ['btn13', 'm', 840, 595], ['btn14', 'n', 0, 645], ['btn15', 'o', 70, 645],
          ['btn16', 'p', 140, 645], ['btn17', 'q', 210, 645], ['btn18', 'r', 280, 645], ['b19', 's', 350, 645], ['btn20', 't', 420, 645],
          ['btn21', 'u', 490, 645], ['btn22', 'v', 560, 645], ['btn23', 'w', 630, 645], ['btn24', 'x', 700, 645], ['b25', 'y', 770, 645],
          ['b26', 'z', 840, 645]]

for p1 in Button:
    exec(
        '{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#ffffe7",activebackground="#ffffe7",font=10,image={})'.format(
            p1[0], p1[1], p1[0], p1[1]))
    exec('{}.place(x={},y={})'.format(p1[0], p1[2], p1[3]))

hang = [['c1', 'h1'], ['c2', 'h2'], ['c3', 'h3'], ['c4', 'h4'], ['c5', 'h5'], ['c6', 'h6'], ['c7', 'h7']]
for p1 in hang:
    exec('{}=Label(root,bg="#ffffe7",image={})'.format(p1[0], p1[1]))

c1.place(x=300, y=-50)

E1 = PhotoImage(file='exit.png')
Ex = Button(root, bd=0, command=root.destroy, bg="#ffffe7", activebackground="#ffffe7", font=10, image=E1)
Ex.place(x=770, y=10)
s2 = 'SCORE:' + str(score)
s1 = Label(root, text=s2, bg="#ffffe7", font=("arial", 25))
s1.place(x=10, y=10)

root.mainloop()

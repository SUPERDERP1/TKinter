from tkinter import *
import random as r
from wordlist import wordlist
import time
text = []
win = Tk()
win.geometry("800x600")
def caesar():
    global alphabetmod, text, icaoAns
    text = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabetmod = []
    modnum = r.randint(1,25)
    for i in range (modnum):
        alphabetmod.append(alphabet[0])
        alphabet.pop(0)
    for i in range (26-modnum):
        alphabetmod.insert(0, alphabet[-1])
        alphabet.pop(-1)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    icaoAns = ''.join(icaoAns)
    qList = icaoAns
    for i in range(len(qList)):
        match qList[i]:
            case "a":
                text.append(alphabetmod[1])
            case "b":
                text.append(alphabetmod[2])
            case "c":
                text.append(alphabetmod[3])
            case "d":
                text.append(alphabetmod[4])
            case "e":
                text.append(alphabetmod[5])
            case "f":
                text.append(alphabetmod[6])
            case "g":
                text.append(alphabetmod[7])
            case "h":
                text.append(alphabetmod[8])
            case "i":
                text.append(alphabetmod[9])
            case "j":
                text.append(alphabetmod[10])
            case "k":
                text.append(alphabetmod[11])
            case "l":
                text.append(alphabetmod[12])
            case "m":
                text.append(alphabetmod[13])
            case "n":
                text.append(alphabetmod[14])
            case "o":
                text.append(alphabetmod[15])
            case "p":
                text.append(alphabetmod[16])
            case "q":
                text.append(alphabetmod[17])
            case "r":
                text.append(alphabetmod[18])
            case "s":
                text.append(alphabetmod[19])
            case "t":
                text.append(alphabetmod[20])
            case "u":
                text.append(alphabetmod[21])
            case "v":
                text.append(alphabetmod[22])
            case "w":
                text.append(alphabetmod[23])
            case "x":
                text.append(alphabetmod[24])
            case "y":
                text.append(alphabetmod[25])
            case "z":
                text.append(alphabetmod[26])
    icao()
def icao():
    global text, icaoAns, randquestion
    icaoAns = []
    randquestion = r.choice(wordlist)
    print(randquestion)
    for i in range(len(list(randquestion))):
        match randquestion[i]:
            case "a":
                icaoAns.append("alfa")
            case "b":
                icaoAns.append("bravo")
            case "c":
                icaoAns.append("charlie")
            case "d":
                icaoAns.append("delta")
            case "e":
                icaoAns.append("echo")
            case "f":
                icaoAns.append("foxtrot")
            case "g":
                icaoAns.append("golf")
            case "h":
                icaoAns.append("hotel")
            case "i":
                icaoAns.append("india")
            case "j":
                icaoAns.append("juliett")
            case "k":
                icaoAns.append("kilo")
            case "l":
                icaoAns.append("lima")
            case "m":
                icaoAns.append("mike")
            case "n":
                icaoAns.append("november")
            case "o":
                icaoAns.append("oscar")
            case "p":
                icaoAns.append("papa")
            case "q":
                icaoAns.append("quebec")
            case "r":
                icaoAns.append("romeo")
            case "s":
                icaoAns.append("sierra")
            case "t":
                icaoAns.append("tango")
            case "u":
                icaoAns.append("uniform")
            case "v":
                icaoAns.append("victor")
            case "w":
                icaoAns.append("whiskey")
            case "x":
                icaoAns.append("xray")
            case "y":
                icaoAns.append("yankee")
            case "z":
                icaoAns.append("zulu")
count = 1
score = 0
submitted = True
def submit():
    global count, submitted, txtin, correct, text, label, score
    txtentry = txtin.get()
    txtentry = txtentry.lower().strip()
    
    text = ''.join(text)
    match count:
        case 0:
            correct = randquestion
        case 1:
            correct = randquestion
            win.config(bg="light blue")
        case 2:
            correct = randquestion
            win.config(bg="lime green")
        case 3:
            correct = randquestion
            win.config(bg="pink")
        case 4:
            correct = randquestion
            win.config(bg="yellow")
    if txtentry == correct:
        winmsg = Label(text="Correct")
        winmsg.update()
        time.sleep(3)
        winmsg.config(text="")
        score += 1
    count += 1
    icao()
    caesar()
    label.config(text=text)
    label.update()
    scoretxt.config(text=score)
    scoretxt.update()
icao()
caesar()
label = Label(win, text=text)
label.pack()  
scoretxt = Label(win, text=score)
submitbtn = Button(win, text = "Submit", command=submit).place(x = 350, y = 170) 
txtin = Entry(win)
scoretxt.pack()
winmsg = Label(text="")
winmsg.pack()
txtin.place(x = 300, y = 130)
win.mainloop()
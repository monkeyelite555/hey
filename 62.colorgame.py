import tkinter
import random
#label.config() will change the text of the label
colors=["Red","Blue","Green","Yellow","Purple","Orange","White","Black","Gray","Pink","Brown"]
timeleft=30
score=0

def startGame(event):
    if timeleft==30:
        countdown()
    nextColor()

def nextColor():
    global score
    global timeleft
    if timeleft>0:
        e.focus_set()
        if e.get().lower() ==colors[1].lower():
            score+=1
        e.delete(0,tkinter.END)
        random.shuffle(colors)
        coloredLabel.config(fg=str(colors[1]),text=str(colors[0]))
        scoreLabel.config(text="Score: "+str(score))

def countdown():
    global timeleft
    if timeleft>0:
        timeleft-=1
        timeLabel.config(text="Time left: "+ str(timeleft))
        timeLabel.after(1000,countdown)

#this goes at the end
root=tkinter.Tk()
root.title("Color Game")
root.geometry("750x400")
instructions=tkinter.Label(root,text="Type in the color ""of the word, not the text!")
instructions.pack()
scoreLabel=tkinter.Label(root,text="Press enter to start",font=("Helvetica",24))
scoreLabel.pack()
timeLabel=tkinter.Label(root,text="Time left: "+str(timeleft),font=("Helvetica",24))
timeLabel.pack()
coloredLabel=tkinter.Label(root,font=("Helvetica",120))
coloredLabel.pack()


e=tkinter.Entry(root)
root.bind("<Return>",startGame)
e.pack()
e.focus_set()
root.mainloop()
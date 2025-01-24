from tkinter import Label, Tk
import time
window=Tk()
window.title("Clock")
window.geometry("420x150")
window.resizable(1,1)
font=("Boulder",98,'bold')
bgcol="#f2e750"
textcol="#363529"
width=25
clock=Label(window,font=font,bg=bgcol,fg=textcol,bd=width)
clock.grid(row=0,column=1)

def digitalclock():
    time_live=time.strftime("%H:%M:%S")
    window.config(bg=bgcol)
    clock.config(text=time_live)
    clock.after(200,digitalclock)

digitalclock()
window.mainloop()
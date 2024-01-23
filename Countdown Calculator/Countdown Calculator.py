from playsound import playsound
import datetime
from tkinter import *
root=Tk()
root.title("Count down timmer")
root.config(background="white")
root.geometry('500x500')
root.resizable(False,False)

#image of Stopwatch
timer_image=PhotoImage(file='C:\\Users\\Admin\\Desktop\\My projets\\Countdown Calculator\\timer img.png')
Label(image=timer_image).place(x=0,y=-25)

#label of timmer
Label(text="Timmer",fg="Black",font=('Kalinga',17),bg='#C9C9C9').place(x=210,y=180)
#label time
h=Label(text="00",fg="Black",font=('Vrinda',30),bg='#C9C9C9')
m=Label(text="00",fg="Black",font=('Vrinda',30),bg='#C9C9C9')
s=Label(text="00",fg="Black",font=('Vrinda',30),bg='#C9C9C9')
h.place(x=169,y=220)
m.place(x=228,y=220)
s.place(x=288,y=220)
Label(text=":",fg="#0F42FD",font=('Lithos Pro Regular',30),bg='#C9C9C9').place(x=215,y=217)
Label(text=":",fg="#0F42FD",font=('Lithos Pro Regular',30),bg='#C9C9C9').place(x=273,y=217)

#Btn to start timmer
start_btn=Button(text="  ",font=(10),bg='#C9C9C9')
start_btn.place(height=21,width=27,x=237,y=102)
root.mainloop()
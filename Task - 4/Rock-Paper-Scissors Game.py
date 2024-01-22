from tkinter import *
from tkinter.ttk import *
import random
a=5
root=Tk()
root.geometry("600x500")
root.configure(bg="white")

def input(button_value):
    input_BOX_2.config(image=button_value)

def play_button_f(button_value):
           if button_value=="":
                 play_button.config(state=DISABLED)

           else:
              play_button.config(state=NORMAL)

              
def c_choice(a) :
     a=random.randint(0,3)
     if a==0 :
          input_BOX_1.config(image=rock)
     if a==1 :
          input_BOX_1.config(image=paper)

     if a==2:
          input_BOX_1.config(image=scis)
        

rock=PhotoImage(file='C:\\Users\\Admin\\Desktop\\rock.png' )
scis=PhotoImage(file='C:\\Users\\Admin\\Desktop\\s.png' )
paper=PhotoImage(file='C:\\Users\\Admin\\Desktop\\paper.png' )
photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\paper.png' )
comp=PhotoImage(file='C:\\Users\\Admin\\Desktop\\comp.png')
user=PhotoImage(file='C:\\Users\\Admin\\Desktop\\user.png')

input_BOX_1=Label(root,image=comp)
input_BOX_1.place(x=80,y=70)
input_BOX_2=Label(root,image=user)
input_BOX_2.place(x=300,y=70)
Label(text="Rock, Paper, Scissors Game",font=("Arial", 30),foreground="#FB910D",background="white").place(x=10 ,y=0)

#Label(text="Score Board",font=("Arial", 20),foreground="Black",background="white").place(x=400 ,y=0)
u_score=Label(text="User Score",font=("Arial", 10),foreground="Black",background="white")
u_score.place(x=310 ,y=210)
c_score=Label(text="Computer Score",font=("Arial", 10),foreground="Black",background="white").place(x=10 ,y=210)

#icons
Button(image=rock,command=lambda:input(rock)).place(x=50,y=270,height=100,width=100)
Button(image=scis,command=lambda:input(scis)).place(x=200,y=270,height=100,width=100)
Button(image=paper,command=lambda:input(paper)).place(x=350,y=270,height=100,width=100)

#play button
play_button=Button(text="Play",command=lambda:c_choice(a))
play_button.place(x=210,y=220)
root.mainloop()
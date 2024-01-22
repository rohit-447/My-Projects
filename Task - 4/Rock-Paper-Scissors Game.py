from tkinter import *
from tkinter import messagebox
import random

#variables
a=0                    #ramdon by computer                    
u_choice=0             #input taken from user
computer_score=0       #score of computer
user_score=0           #score of user
match_played=0         #no of matches played
bttn=0                 #argument used in reset fun
play_button_value=0    #argument used in play button
no_input=0             #argument used in no_input fun


#window configuration
root=Tk()
root.geometry("600x500")
root.configure(bg="white")

#reset button
def reset(bttn):
     global computer_score
     global user_score
     global match_played
     global play_button_value
     computer_score=0
     user_score=0
     match_played=0
     u_choice=4
     if bttn==0:
      winner.config(text="None")
      match_played_score.config(text=match_played)
      input_BOX_2.config(image=user)
      input_BOX_1.config(image=comp)
      c_score_label.config(text=computer_score)
      u_score_label.config(text=user_score)
      if u_choice==4:
           play_button_value=1
           print("reset",play_button_value)
           no_output(play_button_value)
     return user_score,computer_score,u_choice,play_button_value
     

#throw an error if no input is provided
def no_output(no_input):
      global play_button_value
      global u_choice

      print('play_button_value',play_button_value)
      print('no_input',no_input)
      if play_button_value==0:
              messagebox.showerror(title="Invalid",message="No input")
      elif play_button_value==1:
              messagebox.showinfo(title="Invalid",message="Game Restarted")
              play_button_value=0
              play_button.config(command=lambda:no_output(play_button_value))
              return u_choice

      elif play_button_value==3:
              print("msg else block")
              play_button.config(command=lambda:c_choice())


#computer random choice        
def c_choice() :
     global a
     global computer_score
     global user_score
     
     a=random.randint(1,3)
     if a==1 :
           input_BOX_1.config(image=rock)
     if a==2 :
           input_BOX_1.config(image=scis)
     if a==3:
          input_BOX_1.config(image=paper)
     scoreboard(user_score,computer_score)
     return a

#it display the input of user
def input(button_value):
    global u_choice
    global play_button_value
    play_button_value=3
    input_BOX_2.config(image=button_value)

    if button_value==rock:
         u_choice=1
    elif button_value==scis:
         u_choice=2
    elif button_value==paper:
         u_choice=3
    else:
         u_choice=4
         play_button_value=1
         play_button.config(command=lambda:no_output(play_button_value))

    print(play_button_value)
    return u_choice,play_button_value

#Logic
def scoreboard(u,c):
     global a
     global u_score
     global c_score
     global user_score
     global computer_score
     global match_played
     match_played=match_played+1
     #tie
     if a==u_choice:
          u_score_label.config(text=user_score)
          c_score_label.config(text=computer_score)

     #rock beats scisssors-1
     if a==1 and u_choice==2:
          computer_score=computer_score+1
          u_score_label.config(text=user_score)
          c_score_label.config(text=computer_score)

     #paper beats rock-1
     if a==1 and u_choice==3:
          computer_score=computer_score+1
          u_score_label.config(text=user_score)
          c_score_label.config(text=computer_score)

     #rock beats scissor-2
     if a==2 and u_choice==1:
          user_score=user_score+1
          u_score_label.config(text=user_score)
          c_score_label.config(text=computer_score)

     #scissor beats rock-2
     if a==2 and u_choice==3:
          computer_score=computer_score+1
          u_score_label.config(text=user_score)
          c_score_label.config(text=computer_score)

      #paper beats rock-2
     if a==3 and u_choice==1:
          computer_score=computer_score+1
          u_score_label.config(text=user_score)
          c_score_label.config(text=computer_score)

     #scissors beats paper-2 
     if a==3 and u_choice==2:
          user_score=user_score+1
          u_score_label.config(text=user_score)
          c_score_label.config(text=computer_score)
     winner_display(computer_score,user_score,match_played)
     a=0
     return a, computer_score,user_score,u_choice

#display the winner
def winner_display(e,f,g):
     if e > f:
        winner.config(text="Computer")          
     elif e<f:
        winner.config(text="User")
     elif  e==f:
          winner.config(text="Match Draw")
     match_played_score.config(text=g)

     
#heading
Label(text="Rock, Paper, Scissors Game", font=("Arial", 30), foreground="#FB910D", background="white").place(x=10, y=0)

#image files
rock=PhotoImage(file='C:\\Users\\Admin\\Desktop\\rock.png' )
scis=PhotoImage(file='C:\\Users\\Admin\\Desktop\\s.png' )
paper=PhotoImage(file='C:\\Users\\Admin\\Desktop\\paper.png' )
photo=PhotoImage(file='C:\\Users\\Admin\\Desktop\\paper.png' )
comp=PhotoImage(file='C:\\Users\\Admin\\Desktop\\comp.png')
user=PhotoImage(file='C:\\Users\\Admin\\Desktop\\user.png')

#display user and computer profile
input_BOX_1=Label(root,  image=comp)
input_BOX_2=Label(root,  image=user)
input_BOX_1.place(x=80,  y=70)
input_BOX_2.place(x=300, y=70)

#scoreboard Label
Label(text="User Score :",    font=("Arial", 10), foreground="Black", background="white").place(x=310 ,y=210)
Label(text="Computer Score :",font=("Arial", 10), foreground="Black", background="white").place(x=10  ,y=210)

#score
c_score_label=Label(text=computer_score, font=("Arial", 10), foreground="Black", background="white")
u_score_label=Label(text=user_score,     font=("Arial", 10), foreground="Black", background="white")
u_score_label.place(x=385, y=210)
c_score_label.place(x=115, y=210)

#winner and no. of matches played board
#winner Label
winner=Label(text="None",        font=("Arial", 15), foreground="Blue", background="white")
winner_box=Label(text="Winner :",font=("Arial", 15), foreground="Blue", background="white")
winner.place(    x=95, y=430)
winner_box.place(x=10, y=430)

#matched played label
match_played_box=Label(text="No.of matches played:",font=("Arial", 15), foreground="Blue", background="white")
match_played_score=Label(text="0",                  font=("Arial", 15), foreground="Blue", background="white")
match_played_box.place(x=10,    y=400)
match_played_score.place(x=210, y=400)

#buttons
#rock,scissor,paper button
btn_1=Button(image=rock,  command=lambda:input(rock))
btn_2=Button(image=scis,  command=lambda:input(scis))
btn_3=Button(image=paper, command=lambda:input(paper))
btn_1.place(x=50,  y=270,  height=100, width=100)
btn_2.place(x=200, y=270,  height=100, width=100)
btn_3.place(x=350, y=270,  height=100, width=100)

#reset button
reset_button=Button(text="Reset", foreground="red", command=lambda:reset(bttn))
reset_button.place(x=250, y=450)

#play button
play_button=Button(text="Play", command=lambda :no_output(play_button_value))
play_button.place(x=210, y=220)

root.mainloop()
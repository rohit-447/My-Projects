from tkinter import *
root=Tk()
root.title("Task-2 Calculator")
root.geometry("290x454")
#root.resizable(FALSE,FALSE)

display=''

#to display input and output
def output(button_value):
    global display
    display=display+button_value
    OUTPUT_BOX.config(text=display)

    #to evaluate value when required
    if button_value == "":
          try:
              result=eval(display)
              OUTPUT_BOX.config(text=result)
    
          except SyntaxError :  
                if len(display)==1 and display[0]=="/" or "*" or "%" :
                 OUTPUT_BOX.config(text="")
                
                else:
                 OUTPUT_BOX.config(text="Invalid")

          finally :
              display=""
                    
#to clear the display
    elif button_value == "C":
     display=""
     OUTPUT_BOX.config(text="")
     display=""

#to display input and output
OUTPUT_BOX=Label(root,height=2,width=14,background="black",fg="white",font=("Arial", 25))
OUTPUT_BOX.place(x=7,y=5)

#column 1
Button(root, text="C", font=("Arial", 30), fg="#FB910D", bd=4, bg="white", command=lambda: output("C")).place(height=70, width=70,  x=1, y=92)
Button(root, text="7", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("7")).place(height=70, width=70,  x=2, y=164)
Button(root, text="4", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("4")).place(height=70, width=70,  x=2, y=236)
Button(root, text="1", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("1")).place(height=70, width=70,  x=2, y=308)
Button(root, text="0", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("0")).place(height=70, width=140, x=2, y=380)

#column 2
Button(root, text="/", font=("Arial", 30), fg="#FB910D", bd=4, bg="white", command=lambda: output("/")).place(height=70, width=70,  x=72, y=92)
Button(root, text="8", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("8")).place(height=70,  width=70,  x=72, y=164)
Button(root, text="5", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("5")).place(height=70,  width=70,  x=72, y=236)
Button(root, text="2", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("2")).place(height=70,  width=70,  x=72, y=308)

#column 3
Button(root, text="%", font=("Arial", 30), fg="#FB910D", bd=4, bg="white", command=lambda: output("%")).place(height=70,  width=70,  x=144, y=92)
Button(root, text="9", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("9")).place(height=70,  width=70,  x=144, y=164)
Button(root, text="6", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("6")).place(height=70,  width=70,  x=144, y=236)
Button(root, text="3", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("3")).place(height=70,  width=70,  x=144, y=308)
Button(root, text=".", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output(".")).place(height=70,  width=70,  x=144, y=380)

#column 4
Button(root, text="x", font=("Arial", 30), fg="#FB910D", bd=4, bg="white", command=lambda: output("*")).place(height=70,  width=70,  x=216, y=92)
Button(root, text="-", font=("Arial", 30), fg="#FB910D", bd=4, bg="white", command=lambda: output("-")).place(height=70,  width=70,  x=216, y=164)
Button(root, text="+", font=("Arial", 30), fg="#FB910D", bd=4, bg="white", command=lambda: output("+")).place(height=70,  width=70,  x=216, y=236)
Button(root, text="=", font=("Arial", 30), fg="white",   bd=4, bg="#FB910D", command=lambda: output("")).place(height=144, width=70,  x=216, y=308)

root.mainloop()
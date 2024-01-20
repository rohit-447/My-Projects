from tkinter import *
root=Tk()
root.title("Task-2 Calculator")
root.geometry("290x478")
#root.resizable(FALSE,FALSE)
display=''
def output(button_value):
    global display
    display=display+button_value
    OUTPUT_BOX.config(text=display)

OUTPUT_BOX=Label(root,height=6,width=40,bg="white")
OUTPUT_BOX.place(x=0,y=0)

#column 1
Button(root, text="C", font=("Arial", 30), fg="#FB910D", bd=4, bg="white", command=lambda: output("C")).place(height=70, width=70,  x=2, y=112)
Button(root, text="7", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("7")).place(height=70, width=70,  x=2, y=184)
Button(root, text="4", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("4")).place(height=70, width=70,  x=2, y=256)
Button(root, text="1", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("1")).place(height=70, width=70,  x=2, y=328)
Button(root, text="0", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("0")).place(height=70, width=140, x=2, y=402)

#column 2
Button(root, text="/", font=("Arial", 30), fg="#FB910D", bd=4, bg="white", command=lambda: output("/")).place(height=70, width=70,  x=72, y=112)
Button(root, text="8", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("8")).place(height=70,  width=70,  x=72, y=184)
Button(root, text="5", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("5")).place(height=70,  width=70,  x=72, y=256)
Button(root, text="2", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("2")).place(height=70,  width=70,  x=72, y=328)

#column 3
Button(root, text="%", font=("Arial", 30), fg="#FB910D", bd=4, bg="white", command=lambda: output("%")).place(height=70,  width=70,  x=144, y=112)
Button(root, text="9", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("9")).place(height=70,  width=70,  x=144, y=184)
Button(root, text="6", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("6")).place(height=70,  width=70,  x=144, y=256)
Button(root, text="3", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output("3")).place(height=70,  width=70,  x=144, y=328)
Button(root, text=".", font=("Arial", 30), fg="black",   bd=4, bg="white", command=lambda: output(".")).place(height=70,  width=70,  x=144, y=402)

#column 4
Button(root, text="x", font=("Arial", 30), fg="#FB910D", bd=4, bg="white", command=lambda: output("*")).place(height=70,  width=70,  x=216, y=112)
Button(root, text="-", font=("Arial", 30), fg="#FB910D", bd=4, bg="white", command=lambda: output("-")).place(height=70,  width=70,  x=216, y=184)
Button(root, text="+", font=("Arial", 30), fg="#FB910D", bd=4, bg="white", command=lambda: output("+")).place(height=70,  width=70,  x=216, y=256)
Button(root, text="=", font=("Arial", 30), fg="#FB910D", bd=4, bg="white", command=lambda: output("=")).place(height=144, width=70,  x=216, y=328)

root.mainloop()
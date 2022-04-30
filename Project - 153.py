from tkinter import *
import random

root=Tk()
root.title("Multidimensional Lists")
root.geometry("400x400")

entry = Entry(root)
label = Label(root)
label1 = Label(root)

array_3d = [[['1','2','3','4','5','6'],["Head","Tail"],["A","B","C","D","E","F","G","H"]]]
print(array_3d[0][0][2])

def new_password():
    label1["text"] = "Guessed Word: " + entry.get()
    
    random1 = random.randint(0,5)
    random2 = random.randint(0,1)
    random3 = random.randint(0,7)
    
    letter1 = str(array_3d[0][0][random1])
    letter2 = str(array_3d[0][1][random2])
    letter3 = str(array_3d[0][2][random3])
    label["text"] = "Generated Password: " + letter1 + "" + letter2 + "" + letter3
    
btn = Button(root,text="New Password", command=new_password)
entry.place(relx=0.5, rely=0.3, anchor=CENTER)
btn.place(relx = 0.5, rely=0.4, anchor=CENTER)
label1.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx = 0.5, rely = 0.6, anchor=CENTER)

root.mainloop()
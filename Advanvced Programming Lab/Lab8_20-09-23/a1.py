from tkinter import *
import random


Questions = ["In a website browser address bar, what does “www” stand for?",
             "In what year were the first Air Jordan sneakers released?",
             "Which African country was formerly known as Abyssinia?",
             "In which European city would you find Orly airport?"]
options = [["wide world web", "world wide web", "world web wide"],
           ["1987","1983","1984"],
           ["Kenya","Egypt","Ethiopia"],
           ["Paris","Barcelona","Brussels"]]
answer = ["world wide web","1984","Ethiopia","Paris"]
num = random.randrange(0,len(Questions))
global flag
flag = None

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master, height=300,width=600)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        self.text_Label = Label(self,text="Welcome to the Quiz!").grid()
        self.text_Label = Label(self,text=Questions[num]).grid()
        global var
        var = StringVar()
        self.R1 = Radiobutton(self, text=options[num][0], variable=var, value=options[num][0]).grid()
        self.R2 = Radiobutton(self, text=options[num][1], variable=var, value=options[num][1]).grid()
        self.R3 = Radiobutton(self, text=options[num][2], variable=var, value=options[num][2]).grid()
        var.set(1)
        self.submit = Button(self, text="Submit", command = self.submit).grid()
        
    def submit(self):
        opt = var.get()
        global flag
        if flag:
            self.text_Label.destroy()
        flag = False
        if(opt == answer[num]):
            self.text_Label = Label(self,text="Correct Answer!")
        else:
            self.text_Label = Label(self,text="Wrong Answer!")
        flag = True
        self.text_Label.grid()
        
    
def main():
    app = Application()
    app.mainloop()
    
if __name__ == '__main__':
    main()
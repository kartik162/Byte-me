from tkinter import *

from tkinter import messagebox as mb
import json
score=0
lst=[]

class Quiz:

    def __init__(self):
        self.q_no=0
        self.display_title()
        self.display_question()
        self.opt_selected=IntVar()
        self.opts=self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size=len(question)
    def display_result(self):
        score=sum(lst)
        if(score>=15):
            result="Please contact a counsellor for futher hep."
        else:
            result="You are doing well. TakeCare and if any assistance is required then contact counsellor"
        mb.showinfo("Result:",f"{result}")
    def check_ans(self, q_no,score):
            if(self.opt_selected.get()==1):
                score+=5
            elif(self.opt_selected.get()==2):
                score+=0
            lst.append(score)
    def next_btn(self):

        self.check_ans(self.q_no,score)
        self.q_no += 1
        if self.q_no==self.data_size:
            self.display_result()
            gui.destroy()
        else:
            self.display_question()
            self.display_options()
    def buttons(self):
        next_button = Button(gui, text="Next",command=self.next_btn,
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        next_button.place(x=350,y=380)
        quit_button = Button(gui, text="Quit", command=gui.destroy,
        width=5,bg="black", fg="white",font=("ariel",16," bold"))
        quit_button.place(x=700,y=50)
    def display_options(self):
        val=0
        self.opt_selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1
    def display_question(self):
        q_no = Label(gui, text=question[self.q_no], width=60,
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
        q_no.place(x=70, y=100)
    def display_title(self):
        title = Label(gui, text="Analyse Absences",
        width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)
    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 2:
            radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",14))
            q_list.append(radio_btn)
            radio_btn.place(x = 100, y = y_pos)
            y_pos += 40
        return q_list
gui = Tk()
gui.geometry("800x450")
gui.title("Questionnaire")
data={
    "question": [
    "Q1. what is your average Attendance?",
    "Q2. Have you ever been diagnosed with a mental disorder before?",
    "Q3. How many hours do you sleep per day?",
    "Q4. During the past 4 weeks have you had any problems with your daily routine at school or home?",
    "Q5. Are you feeling tired or having little energy?",
    "Q6. Are you having a poor appetite?"],
    "options": [
        ["Less than 80%","80% and Above",],
        ["Yes","No"],
        ["Less than 6 hours","6hours+"],
        ["Yes","No"],
        ["Yes","No"],
        ["Yes","No"]]}
question = (data['question'])
options = (data['options'])
quiz = Quiz()
gui.mainloop()


# coding: utf-8

# In[134]:


import os
import tkinter as tk
from tkinter import messagebox
from tkinter import *
class Module:
    def __init__(self, name, code):
        self.name=name
        self.code = code

class Question:
    def __init__(self, typ, description,score):
        self.typ= typ
        self.description=description          
        self.score=score
class MCQs(Question):
    def __init_(self,options,desp, typ,score):
        super.__init__(typ, desp,score)
        self.options=options
class TF(Question):
    def __init_(self,correct_option,desp, typ,score):
        super.__init__(typ, desp,score)
        self.options=options
class BestMatch(Question):
    def __init_(self,options,desp, typ):
        super.__init__(typ, desp,score)
        self.options=options
        
# function to clsoe the window    
def close(r):
    r.destroy()
# function to clear window
def clear_window(root):
    list = root.grid_slaves()
    for l in list:
        l.destroy()
    return root
def checkAlreadyModuleExist(filename, code, name): # function to check if course already exists
    if not os.path.exists(filename + '.txt'):
        return False
    f = open(filename + '.txt', "r")
    for i in f.readlines():
        ls =i.split("\t")
    if (ls[0]==code and ls[1].replace("\n","")==name):
        return True 
    return False

def Add_Module_in_file(filename, code, name):
    if checkAlreadyModuleExist(filename,code,name): # check if the module is already added
        messagebox.showinfo("Module Error", "Module is already there")
        return False
    else:
        with open(filename+".txt", 'a') as f: # if module not added, then add 
            f.write(code+"\t"+name+"\n")
        f.close()
        return True
def get_modules(filename):
    code_ls = [] # list to hold codes
    dc={} # dictionary hold hold code,name as pair
    f = open(filename+".txt","r").readlines()
    for i in f:
        j = i.split("\t")
        code_ls.append(j[0])
        dc[j[0]] =j[1].replace("\n","")
    return code_ls,dc
def Edit_Module(root):
    root = clear_window(root)
    root.title("Calculate")
    # Create a Tkinter variable
    tkvar = StringVar(root)
    ls, dc = get_modules("modules")
    # Dictionary with options
    choices = {i for i in ls}
    tkvar.set('None')  # set the default option
    popupMenu = OptionMenu(root, tkvar, *choices)
    Label(root, text="Please choose",font=("Helvetica", 15)).grid(row=2, column=2)
    popupMenu.grid(row=3, column=2)
    b2 = Button(root, text='Edit', command=lambda:changed_Val(tkvar,dc,root))
    b2.grid(row=6, column=2)
    Button(root, text='Back', command=lambda:Module_management(root)).grid(row=7, column=2)
    root.mainloop()
def delete_Module(root):
    root= clear_window(root)
    root.title("Delete Module")
    # Create a Tkinter variable
    tkvar = StringVar(root)
    ls, dc = get_modules("modules")
    # Dictionary with options
    choices = {i for i in ls}
    tkvar.set('None')  # set the default option

    popupMenu = OptionMenu(root, tkvar, *choices)
    Label(root, text="Please choose",font=("Helvetica", 15)).grid(row=2, column=2)
    popupMenu.grid(row=3, column=2)
    b2 = Button(root, text='Delete', command=lambda:changed_Val_Del(tkvar,dc,root))
    b2.grid(row=6, column=2)
    Button(root, text='Back', command=lambda:Module_management(root)).grid(row=7, column=2)
    root.mainloop()
def changed_Val_Del(tkvar,dc, frame):
    if tkvar.get() == 'None':
        messagebox.showinfo("Module Error", "Select the module to delete")
    else:
        list = frame.grid_slaves()
        for l in list:
            l.destroy()
        save_module(dc,tkvar.get(), dc[tkvar.get()], frame, "del")
    
def save_module(dc, ky, val,frame, op):
    if op=="del":
        del dc[ky]
    else:
        dc[ky]=val
    with open("modules.txt", 'w') as f:
        
        for k in dc.keys():
            f.write(k+"\t"+dc[k]+"\n")
        f.close()
    messagebox.showinfo("Module saved", "Module are updated successfully")
    if op=="del":
        delete_Module(frame)
    else:
        Edit_Module(frame)
    
def changed_Val(tkvar,dc, frame):
    
    if tkvar.get() == 'None':
        messagebox.showinfo("Module Error", "Select the module")
    else:
        frame= clear_window(frame)
        frame.title("Edit module name")
        Label(frame,text="Edit Name ",justify='center',font=("Helvetica", 15)).grid(row=1, column=0)
        cod = StringVar()
        cod.set(dc[tkvar.get()])
        Entry(frame, textvariable = cod).grid(row=1, column=1, sticky=E)
        Button(frame,text='Save',font=("Helvetica", 18), command=lambda:save_module(dc,tkvar.get(), cod.get(), frame,"sv")).grid(row=2, column=0)
        
# Top level window
def Add_Module(frame):
    list = frame.grid_slaves()
    for l in list:
        l.destroy()
    frame.title("Add Module")   
    Label(frame,text='Add Module',justify='center',font=("Helvetica", 25)).grid(row=0)
    Label(frame,text='Enter Code',justify='center',font=("Helvetica", 15)).grid(row=1,column=0)
    cod = StringVar()
    Entry(frame, textvariable = cod).grid(row=1, column=1, sticky=E)
    Label(frame,text='Enter Module',justify='center',font=("Helvetica", 15)).grid(row=2,column=0)
    nam = StringVar()
    Entry(frame, textvariable = nam).grid(row=2, column=1, sticky=E)
    # Button Creation
    tk.Button(frame,
                            text = "Add",
                            command = lambda:ValidateInput(cod, nam,frame)).grid(row=3,column=0)
    
    tk.Button(frame,
                            text = "Back",
                            command = lambda:Module_management(frame)).grid(row=4,column=0)
    
    frame.mainloop()



def ValidateInput(code, name, root):
    cod = code.get()
    nam = name.get()
    if nam=="" and cod=="":
        messagebox.showerror("Error","Module code and name are missing")  
    elif nam=="":
        messagebox.showerror( "Error","Module name is missing")
    elif cod=="":
        messagebox.showerror("Error", "Module code is missing")
    else:
        st = Add_Module_in_file("modules", cod, nam)
        if st==True:
            messagebox.showinfo("Add module", "Module added successfully!")
            Module_management(root)
# TextBox Creation


def Module_management(root):
    root = clear_window(root)
    root.title("Module Management")
    Label(root,text='Welcome to Module Menu',justify='center',font=("Helvetica", 25)).grid(row=0)
    Label(root,text=' ').grid(row=1)
    rw=2
    Label(root,text='For adding modules =>  ',font=("Helvetica", 18)).grid(row=rw, column=0)
    Button(root,text='Add Module',font=("Helvetica", 18),command=lambda:Add_Module(root)).grid(row=rw, column=1)
    rw+=1
    Label(root,text=' ').grid(row=rw)
    rw+=1
    Label(root,text='For editin module =>  ',font=("Helvetica", 18)).grid(row=rw, column=0)
    Button(root,text='Edit Module',font=("Helvetica", 18),command=lambda:Edit_Module(root)).grid(row=rw, column=1)
    rw+=1
    Label(root,text=' ').grid(row=rw)
    rw+=1
    Label(root,text='For deleting module =>  ',font=("Helvetica", 18)).grid(row=rw, column=0)
    Button(root,text='Delete module',font=("Helvetica", 18),command=lambda:delete_Module(root)).grid(row=rw,column=1)
    root.mainloop()
def changed_Val_Q(modul,q_Type,dc, frame):
    
    if modul.get() == 'None' and q_Type.get()=="None":
        messagebox.showinfo("Selection Error", "Select the module and question type")
    elif q_Type.get() == 'None':
        messagebox.showinfo("Selection Error", "Select the question type")
    elif modul.get() == 'None':
        messagebox.showinfo("Selection Error", "Select the  module ")
    else:
#         MCQ", "TF" , "BestMatch
        if q_Type.get()=="MCQ":
            frame= clear_window(frame)
            frame.title("MCQs")
            Label(frame,text="Write Question",justify='center',font=("Helvetica", 15)).grid(row=1, column=0)
            boxinpt = StringVar(frame)
            Entry(frame, textvariable = boxinpt).grid(row=1, column=1, sticky=E)
            
            Label(frame,text="A",justify='center').grid(row=2, column=0)
            option1 = StringVar(frame)
            Entry(frame, textvariable = option1).grid(row=2, column=1, sticky=E)
            
            Label(frame,text="B",justify='center').grid(row=3, column=0)
            option2 = StringVar(frame)
            Entry(frame, textvariable = option2).grid(row=3, column=1, sticky=E)
            
            Label(frame,text="C",justify='center').grid(row=4, column=0)
            option3 = StringVar(frame)
            Entry(frame, textvariable = option3).grid(row=4, column=1, sticky=E)
            
            Label(frame,text="D",justify='center').grid(row=5, column=0)
            option4 = StringVar(frame)
            Entry(frame, textvariable = option4).grid(row=5, column=1, sticky=E)
            
            Label(frame,text="Choose correct option",justify='center').grid(row=6, column=0)
            
            choice={"A","B","C","D"}
            correct_ans = StringVar(frame)
            correct_ans.set('None')  # set the default option
            OptionMenu(frame, correct_ans, *choice).grid(row=6, column=1)
            options = [option1, option2, option3, option4]
            
            Label(frame,text="Score",justify='center').grid(row=7, column=0)
            score = StringVar(frame)
            Entry(frame, textvariable = score).grid(row=7, column=1, sticky=E)
            Button(frame,text='Save',font=("Helvetica", 18), command=lambda:add_Mcqs(frame,modul,boxinpt,options,correct_ans,score)).grid(row=9, column=1)
        elif q_Type.get()=="TF":
            frame= clear_window(frame)
            frame.title("True / False")
            Label(frame,text="Write Question",justify='center',font=("Helvetica", 15)).grid(row=1, column=0)
            boxinpt = StringVar(frame)
            Entry(frame, textvariable = boxinpt).grid(row=1, column=1, sticky=E)
            
            Label(frame,text="Choose correct option",justify='center').grid(row=6, column=0)
            
            choice={"True","False"}
            correct_ans = StringVar(frame)
            correct_ans.set('None')  # set the default option
            OptionMenu(frame, correct_ans, *choice).grid(row=6, column=1)
            
            Label(frame,text="Score",justify='center').grid(row=7, column=0)
            score = StringVar(frame)
            Entry(frame, textvariable = score).grid(row=7, column=1, sticky=E)
            Button(frame,text='Save',font=("Helvetica", 18), command=lambda:add_TF(frame,modul,boxinpt,correct_ans,score)).grid(row=9, column=1)
        else:
            frame= clear_window(frame)
            frame.title("BestMatch")
            Label(frame,text="Write Question",justify='center',font=("Helvetica", 15)).grid(row=1, column=0)
            boxinpt = StringVar(frame)
            Entry(frame, textvariable = boxinpt).grid(row=1, column=1, sticky=E)
            
            Label(frame,text="A",justify='center').grid(row=2, column=0)
            option1 = StringVar(frame)
            Entry(frame, textvariable = option1).grid(row=2, column=1, sticky=E)
            
            Label(frame,text="B",justify='center').grid(row=3, column=0)
            option2 = StringVar(frame)
            Entry(frame, textvariable = option2).grid(row=3, column=1, sticky=E)
            
            Label(frame,text="C",justify='center').grid(row=4, column=0)
            option3 = StringVar(frame)
            Entry(frame, textvariable = option3).grid(row=4, column=1, sticky=E)
            
            Label(frame,text="D",justify='center').grid(row=2, column=3)
            option4 = StringVar(frame)
            Entry(frame, textvariable = option4).grid(row=2, column=4, sticky=E)
            
            Label(frame,text="E",justify='center').grid(row=3, column=3)
            option5 = StringVar(frame)
            Entry(frame, textvariable = option5).grid(row=3, column=4, sticky=E)
            
            Label(frame,text="F",justify='center').grid(row=4, column=3)
            option6 = StringVar(frame)
            Entry(frame, textvariable = option6).grid(row=4, column=4, sticky=E)
            
            
            Label(frame,text="Write Correct answer: (Format: pairs separated by comma i.e. AE,BD,CE)",justify='center').grid(row=5, column=0)
            correct_ans = StringVar(frame)
            Entry(frame, textvariable = correct_ans).grid(row=5, column=1, sticky=E)
            
            
            options =[option1, option2, option3, option4, option5, option6]
            Label(frame,text="Score",justify='center').grid(row=7, column=0)
            score = StringVar(frame)
            Entry(frame, textvariable = score).grid(row=7, column=1, sticky=E)
            Button(frame,text='Save',font=("Helvetica", 18), command=lambda:add_BestMatch(frame,modul,boxinpt,options,correct_ans,score)).grid(row=9, column=1)
def add_BestMatch(frame,modul,boxinpt,options,correct_ans, score):
    if correct_ans.get()=="None":
        messagebox.showerror("Error", "Write correct answer")
    elif boxinpt.get()=="":
        messagebox.showerror("Error", "Write the question")
    elif options[0].get() =="" or options[1].get() =="" or options[2].get() =="" or options[3].get() =="" or options[4]=="" or options[5]=="": 
        messagebox.showerror("Error", "Option(s) is/are left, please check it again")
    elif score.get()=="":
        messagebox.showerror("Error", "Insert  score")
    else:
        question =boxinpt.get() 
        with open("bestmatch.txt", 'a') as f: # if module not added, then add 
            f.write(modul.get()+"\t"+boxinpt.get()+"\t"+options[0].get()+"\t"+options[1].get()+"\t"+options[2].get()+"\t"+options[3].get()+"\t")
            f.write(options[4].get()+"\t"+options[5].get()+"\t")
            f.write(correct_ans.get()+"\t"+score.get()+"\t\n")
        f.close()
        messagebox.showinfo("Best Match saved", "Best match with answers is updated successfully")
        Question_management(frame)        
            
def add_TF(frame,modul,boxinpt,correct_ans, score):
    if correct_ans.get()=="None":
        messagebox.showerror("Error", "Select correct answer")
    elif boxinpt.get()=="":
        messagebox.showerror("Error", "Write the question")
    elif score.get()=="":
        messagebox.showerror("Error", "Insert  score")
    else:
        question =boxinpt.get() 
        with open("tf.txt", 'a') as f: # if module not added, then add 
            f.write(modul.get()+"\t"+boxinpt.get()+"\t"+correct_ans.get()+"\t"+score.get()+"\t\n")
        f.close()
        messagebox.showinfo("TF saved", "TF type question is updated successfully")
        Question_management(frame)
        
def add_Mcqs(frame,modul,boxinpt,options,correct_ans, score):
    if correct_ans.get()=="None":
        messagebox.showerror("Error", "Select correct answer")
    elif boxinpt.get()=="":
        messagebox.showerror("Error", "Write the question")
    elif options[0].get() =="" or options[1].get() =="" or options[2].get() =="" or options[3].get() =="": 
        messagebox.showerror("Error", "Option(s) is/are left, please check it again")
    elif score.get()=="":
        messagebox.showerror("Error", "Insert  score")
    else:
        question =boxinpt.get() 
        with open("mcqs.txt", 'a') as f: # if module not added, then add 
            f.write(modul.get()+"\t"+boxinpt.get()+"\t"+options[0].get()+"\t"+options[1].get()+"\t"+options[2].get()+"\t"+options[3].get()+"\t")
            f.write(correct_ans.get()+"\t"+score.get()+"\t\n")
        f.close()
        messagebox.showinfo("MCQs saved", "MCQ with answers is updated successfully")
        frame.destroy()
        main_menu()
        
def Add_Question(root):
    root = clear_window(root)
    root.title("Add Question")
    # Create a Tkinter variable
    tkvar = StringVar(root)
    ques_type_select = StringVar(root)
    question_type= {"MCQ", "TF" , "BestMatch"}
    ls, dc = get_modules("modules")
    # Dictionary with options
    choices = {i for i in ls}
    tkvar.set('None')  # set the default option
    ques_type_select.set('None')  # set the default option
    OptionMenu(root, tkvar, *choices).grid(row=3, column=2)
    OptionMenu(root, ques_type_select, *question_type).grid(row=5, column=2)
       
    Label(root, text="Please choose",font=("Helvetica", 15)).grid(row=2, column=2)
    b2 = Button(root, text='Add Question', command=lambda:changed_Val_Q(tkvar,ques_type_select,dc,root))
    b2.grid(row=6, column=2)
    Button(root, text='Back', command=lambda:Question_management(root)).grid(row=7, column=2)
    root.mainloop()
def Edit_Question(root):
    root = clear_window(root)
    root.title("Edit Question")
    # Create a Tkinter variable
    tkvar = StringVar(root)
    ques_type_select = StringVar(root)
    question_type= {"MCQ", "TF" , "BestMatch"}
    ls, dc = get_modules("modules")
    # Dictionary with options
    choices = {i for i in ls}
    tkvar.set('None')  # set the default option
    ques_type_select.set('None')  # set the default option
    OptionMenu(root, tkvar, *choices).grid(row=3, column=2)
    OptionMenu(root, ques_type_select, *question_type).grid(row=5, column=2)
       
    Label(root, text="Please choose",font=("Helvetica", 15)).grid(row=2, column=2)
    b2 = Button(root, text='Edit Question', command=lambda:changed_editq(tkvar,ques_type_select,dc,root))
    b2.grid(row=6, column=2)
    Button(root, text='Back', command=lambda:Question_management(root)).grid(row=7, column=2)
    root.mainloop()
def Delete_Question(root):
    root = clear_window(root)
    root.title("Delete Question")
    # Create a Tkinter variable
    tkvar = StringVar(root)
    ques_type_select = StringVar(root)
    question_type= {"MCQ", "TF" , "BestMatch"}
    ls, dc = get_modules("modules")
    # Dictionary with options
    choices = {i for i in ls}
    tkvar.set('None')  # set the default option
    ques_type_select.set('None')  # set the default option
    OptionMenu(root, tkvar, *choices).grid(row=3, column=2)
    OptionMenu(root, ques_type_select, *question_type).grid(row=5, column=2)
       
    Label(root, text="Please choose",font=("Helvetica", 15)).grid(row=2, column=2)
    b2 = Button(root, text='Delete Question', command=lambda:changed_delete_q(tkvar,ques_type_select,dc,root))
    b2.grid(row=6, column=2)
    Button(root, text='Back', command=lambda:Question_management(root)).grid(row=7, column=2)
    root.mainloop()
def changed_delete_q(modul,q_Type,dc, frame):
    
    if modul.get() == 'None' and q_Type.get()=="None":
        messagebox.showinfo("Selection Error", "Select the module and question type")
    elif q_Type.get() == 'None':
        messagebox.showinfo("Selection Error", "Select the question type")
    elif modul.get() == 'None':
        messagebox.showinfo("Selection Error", "Select the  module ")
    else:
#         MCQ", "TF" , "BestMatch
        if q_Type.get()=="MCQ":
            questions = get_data("mcqs")
            frame= clear_window(frame)
            only_q = list(questions.keys())
            frame.title("Edit MCQs")
            Label(frame,text="Selection question to edit",justify='center',font=("Helvetica", 15)).grid(row=1, column=0)
            correct_ans = StringVar(frame)
            correct_ans.set('None')  # set the default option
            OptionMenu(frame, correct_ans, *only_q).grid(row=1, column=1)
            Button(frame,text='Delete',font=("Helvetica", 18), command=lambda:edit_mcqs(frame,correct_ans,questions,"del")).grid(row=2, column=1)
        elif q_Type.get()=="TF":
            questions = get_data("tf")
            frame= clear_window(frame)
            only_q = list(questions.keys())
            frame.title("Edit TF")
            Label(frame,text="Selection question to edit",justify='center',font=("Helvetica", 15)).grid(row=1, column=0)
            correct_ans = StringVar(frame)
            correct_ans.set('None')  # set the default option
            OptionMenu(frame, correct_ans, *only_q).grid(row=1, column=1)
            Button(frame,text='Delete',font=("Helvetica", 18), command=lambda:edit_TF(frame,correct_ans,questions, "del")).grid(row=2, column=1)
        else:
            questions = get_data("bestmatch")
            frame= clear_window(frame)
            only_q = list(questions.keys())
            frame.title("Edit BestMatch")
            Label(frame,text="Selection question to edit",justify='center',font=("Helvetica", 15)).grid(row=1, column=0)
            correct_ans = StringVar(frame)
            correct_ans.set('None')  # set the default option
            OptionMenu(frame, correct_ans, *only_q).grid(row=1, column=1)
            Button(frame,text='Edit',font=("Helvetica", 18), command=lambda:edit_BM(frame,correct_ans,questions,"del")).grid(row=2, column=1)
def get_data(filename):
    data = open(filename+".txt", "r").readlines()
    questions={}
    for i in data:
        j=i.split("\t")
        j.remove("\n")
        questions[j[1]]= [j[0]]+j[2:]
    return questions

def changed_editq(modul,q_Type,dc, frame):
    
    if modul.get() == 'None' and q_Type.get()=="None":
        messagebox.showinfo("Selection Error", "Select the module and question type")
    elif q_Type.get() == 'None':
        messagebox.showinfo("Selection Error", "Select the question type")
    elif modul.get() == 'None':
        messagebox.showinfo("Selection Error", "Select the  module ")
    else:
#         MCQ", "TF" , "BestMatch
        if q_Type.get()=="MCQ":
            questions = get_data("mcqs")
            frame= clear_window(frame)
            only_q = list(questions.keys())
            frame.title("Edit MCQs")
            Label(frame,text="Selection question to edit",justify='center',font=("Helvetica", 15)).grid(row=1, column=0)
            correct_ans = StringVar(frame)
            correct_ans.set('None')  # set the default option
            OptionMenu(frame, correct_ans, *only_q).grid(row=1, column=1)
            Button(frame,text='Edit',font=("Helvetica", 18), command=lambda:edit_mcqs(frame,correct_ans,questions,"Edit")).grid(row=2, column=1)
        elif q_Type.get()=="TF":
            questions = get_data("tf")
            frame= clear_window(frame)
            only_q = list(questions.keys())
            frame.title("Edit TF")
            Label(frame,text="Selection question to edit",justify='center',font=("Helvetica", 15)).grid(row=1, column=0)
            correct_ans = StringVar(frame)
            correct_ans.set('None')  # set the default option
            OptionMenu(frame, correct_ans, *only_q).grid(row=1, column=1)
            Button(frame,text='Edit',font=("Helvetica", 18), command=lambda:edit_TF(frame,correct_ans,questions,"edit")).grid(row=2, column=1)
        else:
            questions = get_data("bestmatch")
            frame= clear_window(frame)
            only_q = list(questions.keys())
            frame.title("Edit BestMatch")
            Label(frame,text="Selection question to edit",justify='center',font=("Helvetica", 15)).grid(row=1, column=0)
            correct_ans = StringVar(frame)
            correct_ans.set('None')  # set the default option
            OptionMenu(frame, correct_ans, *only_q).grid(row=1, column=1)
            Button(frame,text='Edit',font=("Helvetica", 18), command=lambda:edit_BM(frame,correct_ans,questions,"edit")).grid(row=2, column=1)

            
def edit_BM(frame,correct_ans,dc,op):
    if correct_ans.get()=="None":
        messagebox.showerror("Error", "Select question")
    elif op=="del":
        del dc[correct_ans]
        with open("bestmatch.txt", 'w') as f:
            for k in dc.keys():
                f.write(dc[k][0]+"\t"+k+"\t")
                f.write(dc[k][1]+"\t"+dc[k][2]+"\t")
                f.write(dc[k][3]+"\t"+dc[k][4]+"\t")
                f.write(dc[k][5]+"\t"+dc[k][6]+"\t")
                f.write(dc[k][7]+"\t"+dc[k][8]+"\t\n")
        f.close()
        messagebox.showinfo("MCQs updated", "MCQ with answers is deleted successfully")
        frame.destroy()
        main_menu()
    else:
        frame = clear_window(frame)
        Label(frame,text="question",justify='center',font=("Helvetica", 15)).grid(row=1, column=0)
        question = StringVar(frame)
        question.set(correct_ans.get())
        
        Entry(frame, textvariable = question).grid(row=1, column=1, sticky=E)
        
        Label(frame,text="A",justify='center',font=("Helvetica", 10)).grid(row=2, column=0)
        option1 = StringVar(frame)
        option1.set(dc[correct_ans.get()][1])
        Entry(frame, textvariable = option1).grid(row=2, column=1, sticky=E)
        
        Label(frame,text="B",justify='center',font=("Helvetica", 10)).grid(row=3, column=0)
        option2 = StringVar(frame)
        option2.set(dc[correct_ans.get()][2])
        Entry(frame, textvariable = option2).grid(row=3, column=1, sticky=E)
        
        Label(frame,text="C",justify='center',font=("Helvetica", 10)).grid(row=4, column=0)
        option3 = StringVar(frame)
        option3.set(dc[correct_ans.get()][3])
        Entry(frame, textvariable = option3).grid(row=4, column=1, sticky=E)
        
        Label(frame,text="D",justify='center',font=("Helvetica", 10)).grid(row=5, column=0)
        option4 = StringVar(frame)
        option4.set(dc[correct_ans.get()][4])
        Entry(frame, textvariable = option4).grid(row=5, column=1, sticky=E)
        
        Label(frame,text="C",justify='center',font=("Helvetica", 10)).grid(row=6, column=0)
        option5 = StringVar(frame)
        option5.set(dc[correct_ans.get()][5])
        Entry(frame, textvariable = option5).grid(row=6, column=1, sticky=E)
        
        Label(frame,text="D",justify='center',font=("Helvetica", 10)).grid(row=7, column=0)
        option6 = StringVar(frame)
        option6.set(dc[correct_ans.get()][6])
        Entry(frame, textvariable = option6).grid(row=7, column=1, sticky=E)
        
        
        Label(frame,text="Correct Ans:",justify='center',font=("Helvetica", 10)).grid(row=8, column=0)
        correct= StringVar(frame)
        correct.set(dc[correct_ans.get()][7])
        Entry(frame, textvariable = correct).grid(row=8, column=1, sticky=E)
        
        Label(frame,text="Score : ",justify='center',font=("Helvetica", 10)).grid(row=9, column=0)
        score= StringVar(frame)
        score.set(dc[correct_ans.get()][8])
        options=[]
        Entry(frame, textvariable = score).grid(row=9, column=1, sticky=E)        
        Button(frame,text='Save',font=("Helvetica", 18), command=lambda:save_BM(frame, dc,correct_ans.get(),[option1,option2,option3,option4,option5, option6], correct,score )).grid(row=10, column=0)
def save_BM(frame, dc,question,options, correct,score ):
    dc[question] = [dc[question][0],options[0].get(),options[1].get(),options[2].get(),options[3].get(),options[4].get(),options[5].get(),correct.get(),score.get()]
    with open("bestmatch.txt", 'w') as f:
        for k in dc.keys():
            f.write(dc[k][0]+"\t"+k+"\t")
            f.write(dc[k][1]+"\t"+dc[k][2]+"\t")
            f.write(dc[k][3]+"\t"+dc[k][4]+"\t")
            f.write(dc[k][5]+"\t"+dc[k][6]+"\t")
            f.write(dc[k][7]+"\t"+dc[k][8]+"\t\n")
    f.close()
    messagebox.showinfo("MCQs updated", "MCQ with answers is updated successfully")
    frame.destroy()
    main_menu()
            
def edit_TF(frame,correct_ans,dc, op):
    if correct_ans.get()=="None":
        messagebox.showerror("Error", "Select question")
    elif op=="del":
        del dc[correct_ans.get()]
        with open("tf.txt", 'w') as f:
            for k in dc.keys():
                f.write(dc[k][0]+"\t"+k+"\t")
                f.write(dc[k][1]+"\t"+dc[k][2]+"\t\n")
        f.close()
        messagebox.showinfo("True/False updated", "TF with answers is deleted successfully")
        frame.destroy()
        main_menu()
    else:
        frame = clear_window(frame)
        Label(frame,text="question",justify='center',font=("Helvetica", 15)).grid(row=1, column=0)
        question = StringVar(frame)
        question.set(correct_ans.get())
        
        Entry(frame, textvariable = question).grid(row=1, column=1, sticky=E)
        
        Label(frame,text="Correct Answer",justify='center',font=("Helvetica", 10)).grid(row=2, column=0)
        option1 = StringVar(frame)
        option1.set(dc[correct_ans.get()][1])
        Entry(frame, textvariable = option1).grid(row=2, column=1, sticky=E)        
        Label(frame,text="Score : ",justify='center',font=("Helvetica", 10)).grid(row=3, column=0)
        score= StringVar(frame)
        score.set(dc[correct_ans.get()][2])
        options=[]
        Entry(frame, textvariable = score).grid(row=3, column=1, sticky=E)        
        Button(frame,text='Save',font=("Helvetica", 18), command=lambda:save_TF(frame, dc,correct_ans.get(),option1,score )).grid(row=4, column=0)            
def save_TF(frame, dc,question,correct,score ):
    dc[question] = [dc[question][0],correct.get(),score.get()]
    with open("tf.txt", 'w') as f:
        for k in dc.keys():
            f.write(dc[k][0]+"\t"+k+"\t")
            f.write(dc[k][1]+"\t"+dc[k][2]+"\t\n")
        f.close()
    messagebox.showinfo("True/False updated", "TF with answers is updated successfully")
    frame.destroy()
    main_menu()

        
def edit_mcqs(frame,correct_ans,dc, op):
    if correct_ans.get()=="None":
        messagebox.showerror("Error", "Select question")
    elif op=="del":
        del dc[correct_ans.get()]
        with open("mcqs.txt", 'w') as f:
            for k in dc.keys():
                f.write(dc[k][0]+"\t"+k+"\t")
                f.write(dc[k][1]+"\t"+dc[k][2]+"\t")
                f.write(dc[k][3]+"\t"+dc[k][4]+"\t")
                f.write(dc[k][5]+"\t"+dc[k][6]+"\t\n")
        f.close()
        messagebox.showinfo("MCQs updated", "MCQ with answers is delete successfully")
        Question_management(frame)
    else:
        frame = clear_window(frame)
        Label(frame,text="question",justify='center',font=("Helvetica", 15)).grid(row=1, column=0)
        question = StringVar(frame)
        question.set(correct_ans.get())
        
        Entry(frame, textvariable = question).grid(row=1, column=1, sticky=E)
        
        Label(frame,text="A",justify='center',font=("Helvetica", 10)).grid(row=2, column=0)
        option1 = StringVar(frame)
        option1.set(dc[correct_ans.get()][1])
        Entry(frame, textvariable = option1).grid(row=2, column=1, sticky=E)
        
        Label(frame,text="B",justify='center',font=("Helvetica", 10)).grid(row=3, column=0)
        option2 = StringVar(frame)
        option2.set(dc[correct_ans.get()][2])
        Entry(frame, textvariable = option2).grid(row=3, column=1, sticky=E)
        
        Label(frame,text="C",justify='center',font=("Helvetica", 10)).grid(row=4, column=0)
        option3 = StringVar(frame)
        option3.set(dc[correct_ans.get()][3])
        Entry(frame, textvariable = option3).grid(row=4, column=1, sticky=E)
        
        Label(frame,text="D",justify='center',font=("Helvetica", 10)).grid(row=5, column=0)
        option4 = StringVar(frame)
        option4.set(dc[correct_ans.get()][4])
        Entry(frame, textvariable = option4).grid(row=5, column=1, sticky=E)
        
        Label(frame,text="Correct Ans:",justify='center',font=("Helvetica", 10)).grid(row=6, column=0)
        correct= StringVar(frame)
        correct.set(dc[correct_ans.get()][5])
        Entry(frame, textvariable = correct).grid(row=6, column=1, sticky=E)
        
        Label(frame,text="Score : ",justify='center',font=("Helvetica", 10)).grid(row=7, column=0)
        score= StringVar(frame)
        score.set(dc[correct_ans.get()][6])
        options=[]
        Entry(frame, textvariable = score).grid(row=7, column=1, sticky=E)        
        Button(frame,text='Save',font=("Helvetica", 18), command=lambda:save_mcqs(frame, dc,correct_ans.get(),[option1,option2,option3,option4], correct,score )).grid(row=8, column=0)
def save_mcqs(frame, dc,question,options, correct,score ):
    dc[question] = [dc[question][0],options[0].get(),options[1].get(),options[2].get(),options[3].get(),correct.get(),score.get()]
    with open("mcqs.txt", 'w') as f:
        for k in dc.keys():
            f.write(dc[k][0]+"\t"+k+"\t")
            f.write(dc[k][1]+"\t"+dc[k][2]+"\t")
            f.write(dc[k][3]+"\t"+dc[k][4]+"\t")
            f.write(dc[k][5]+"\t"+dc[k][6]+"\t\n")
        f.close()
    messagebox.showinfo("MCQs updated", "MCQ with answers is updated successfully")
    Question_management(frame)
    
def Question_management(root):
    root = clear_window(root)
    root.title("Question Management")
    Label(root,text='Welcome to Questions Menu',justify='center',font=("Helvetica", 25)).grid(row=0)
    Label(root,text=' ').grid(row=1)
    rw=2
    Label(root,text='For adding questions =>  ',font=("Helvetica", 18)).grid(row=rw, column=0)
    Button(root,text='Add Question',font=("Helvetica", 18),command=lambda:Add_Question(root)).grid(row=rw, column=1)
    rw+=1
    Label(root,text=' ').grid(row=rw)
    rw+=1
    Label(root,text='For editing question =>  ',font=("Helvetica", 18)).grid(row=rw, column=0)
    Button(root,text='Edit Question',font=("Helvetica", 18),command=lambda:Edit_Question(root)).grid(row=rw, column=1)
    rw+=1
    Label(root,text=' ').grid(row=rw)
    rw+=1
    Label(root,text='For deleting question =>  ',font=("Helvetica", 18)).grid(row=rw, column=0)
    Button(root,text='Delete question',font=("Helvetica", 18),command=lambda:Delete_Question(root)).grid(row=rw,column=1)
    root.mainloop()
def main_menu():
    root = Tk()
    root.title("Main Menu")
    Label(root,text='Welcome to Menu',justify='center',font=("Helvetica", 25)).grid(row=0)
    Label(root,text=' ').grid(row=1)
    rw=2
    Label(root,text='For modules Management =>  ',font=("Helvetica", 18)).grid(row=rw, column=0)
    Button(root,text='Modules Management',font=("Helvetica", 18),command=lambda:Module_management(root)).grid(row=rw, column=1)
    rw+=1
    Label(root,text=' ').grid(row=rw)
    rw+=1
    Label(root,text='For questions Management =>  ',font=("Helvetica", 18)).grid(row=rw, column=0)
    Button(root,text='Questions Management',font=("Helvetica", 18),command=lambda:Question_management(root)).grid(row=rw, column=1)
    rw+=1
    Label(root,text=' ').grid(row=rw)
    rw+=1
    Label(root,text='For exit  =>  ',font=("Helvetica", 18)).grid(row=rw, column=0)
    Button(root,text='Exit',font=("Helvetica", 18),command=lambda:close(root)).grid(row=rw,column=1)
    root.mainloop()
main_menu()


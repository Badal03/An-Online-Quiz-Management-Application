# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 17:34:08 2021

@author: Dell
"""
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import mysql.connector 
import time
import datetime
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="Python_project")
mycursor=mydb.cursor()
flag=0
flag1=0
student_flag=0
admin_flag=0

#<--------------------------------------------------------Admin-------------------------------------------------------->
#Add Question
def addquestion():
    ad_menu.destroy()
    global addq
    addq = Tk()
    
    question = StringVar()
    option1 = StringVar()
    option2 = StringVar()
    option3 = StringVar()
    option4 = StringVar()
    answer = StringVar()    
    
    addq_canvas = Canvas(addq,width=720,height=440,bg="blue")
    addq_canvas.pack()

    addq_frame = Frame(addq_canvas,bg="white")
    addq_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(addq_frame,text="Add Question",fg="black",bg="white")
    heading.config(font=('calibri 20'))
    heading.place(relx=0.3,rely=0.1)

    #Question
    qlabel = Label(addq_frame,text="Question :",fg='black',bg='white')
    qlabel.place(relx=0.21,rely=0.3)
    tquestion = Entry(addq_frame,bg='#d3d3d3',fg='black')
    tquestion.config(width=42)
    tquestion.place(relx=0.31,rely=0.3)

    #Option 1
    o1label = Label(addq_frame,text="Option 1:",fg='black',bg='white')
    o1label.place(relx=0.21,rely=0.4)
    toption1 = Entry(addq_frame,bg='#d3d3d3',fg='black')
    toption1.config(width=42)
    toption1.place(relx=0.31,rely=0.4)
    
    
    #Option 2
    o2label = Label(addq_frame,text="option 2:",fg='black',bg='white')
    o2label.place(relx=0.215,rely=0.5)
    toption2 = Entry(addq_frame,bg='#d3d3d3',fg='black')
    toption2.config(width=42)
    toption2.place(relx=0.31,rely=0.5)
    
    
    #Option 3
    o3label = Label(addq_frame,text="option 3:",fg='black',bg='white')
    o3label.place(relx=0.215,rely=0.6)
    toption3 = Entry(addq_frame,bg='#d3d3d3',fg='black')
    toption3.config(width=42)
    toption3.place(relx=0.31,rely=0.6)
    
    #Option 4
    o4label = Label(addq_frame,text="option 4:",fg='black',bg='white')
    o4label.place(relx=0.215,rely=0.7)
    toption4 = Entry(addq_frame,bg='#d3d3d3',fg='black')
    toption4.config(width=42)
    toption4.place(relx=0.31,rely=0.7)
    
    #answer
    anlabel = Label(addq_frame,text="answer:",fg='black',bg='white')
    anlabel.place(relx=0.215,rely=0.8)
    tanswer = Entry(addq_frame,bg='#d3d3d3',fg='black')
    tanswer.config(width=42)
    tanswer.place(relx=0.31,rely=0.8)
    def addquestionToDataBase():
        
        question = tquestion.get()
        option1 = toption1.get()
        option2 = toption2.get()
        option3= toption3.get()
        option4=toption4.get()
        answer=tanswer.get()
        
        global mycursor
        global mydb
        sql="INSERT INTO quiz(question,option_1,option_2,option_3,option_4,answer)VALUES(%s,%s,%s,%s,%s,%s)"
        data=(question,option1,option2,option3,option4,answer)
        mycursor.execute(sql,data)
        mydb.commit()
        if mycursor.rowcount>0:
            messagebox.showinfo("insert Message","Successfully inserted",parent=addq)
        else:
            messagebox.showerror("Error","Question Not inserted",parent=addq)

    #Add BUTTON
    add = Button(addq_frame,text='Add',padx=5,pady=5,width=5,command = addquestionToDataBase,bg='green')
    add.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    add.place(relx=0.2,rely=0.9)
    
    def backhome():
        global admin_flag
        admin_flag=1
        admin_menu()
    #back Button
    back = Button(addq_frame,text='Back',padx=5,pady=5,width=5,bg="green",command=backhome)
    back.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    back.place(relx=0.6,rely=0.9)

    addq.mainloop()
    
    
#update Question
def updatequestion():
    
    ad_menu.destroy()
    global updateq
    updateq = Tk()
    
    qid=StringVar()
    question = StringVar()
    option1 = StringVar()
    option2 = StringVar()
    option3 = StringVar()
    option4 = StringVar()
    answer = StringVar()    
    
    updateq_canvas = Canvas(updateq,width=720,height=440,bg="blue")
    updateq_canvas.pack()

    updateq_frame = Frame(updateq_canvas,bg="white")
    updateq_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(updateq_frame,text="Update Question",fg="black",bg="white")
    heading.config(font=('calibri 20'))
    heading.place(relx=0.3,rely=0.1)

    #id
    qidlabel = Label(updateq_frame,text="Question id :",fg='black',bg='white')
    qidlabel.place(relx=0.17,rely=0.2)
    tqid = Entry(updateq_frame,bg='#d3d3d3',fg='black',textvariable =qid)
    tqid.config(width=42)
    tqid.place(relx=0.31,rely=0.2)
    
    
    #Question
    qlabel = Label(updateq_frame,text="Question :",fg='black',bg='white')
    qlabel.place(relx=0.21,rely=0.3)
    tquestion = Entry(updateq_frame,bg='#d3d3d3',fg='black',textvariable =question)
    tquestion.config(width=42)
    tquestion.place(relx=0.31,rely=0.3)

    #Option 1
    o1label = Label(updateq_frame,text="Option 1 :",fg='black',bg='white')
    o1label.place(relx=0.21,rely=0.4)
    toption1 = Entry(updateq_frame,bg='#d3d3d3',fg='black',textvariable = option1)
    toption1.config(width=42)
    toption1.place(relx=0.31,rely=0.4)
    
    
    #Option 2
    o2label = Label(updateq_frame,text="Option 2 :",fg='black',bg='white')
    o2label.place(relx=0.215,rely=0.5)
    toption2 = Entry(updateq_frame,bg='#d3d3d3',fg='black',textvariable =option2)
    toption2.config(width=42)
    toption2.place(relx=0.31,rely=0.5)
    
    
    
    #Option 3
    o3label = Label(updateq_frame,text="Option 3 :",fg='black',bg='white')
    o3label.place(relx=0.215,rely=0.6)
    toption3 = Entry(updateq_frame,bg='#d3d3d3',fg='black',textvariable = option3)
    toption3.config(width=42)
    toption3.place(relx=0.31,rely=0.6)
    
    
    #Option 4
    o4label = Label(updateq_frame,text="Option 4 :",fg='black',bg='white')
    o4label.place(relx=0.215,rely=0.7)
    toption4 = Entry(updateq_frame,bg='#d3d3d3',fg='black',textvariable = option4)
    toption4.config(width=42)
    toption4.place(relx=0.31,rely=0.7)
    
    #Answer
    anlabel = Label(updateq_frame,text="Answer :",fg='black',bg='white')
    anlabel.place(relx=0.215,rely=0.8)
    tanswer = Entry(updateq_frame,bg='#d3d3d3',fg='black',textvariable = answer)
    tanswer.config(width=42)
    tanswer.place(relx=0.31,rely=0.8)
    def updatequestionToDataBase():
        
        qid=str(tqid.get())
        question = tquestion.get()
        option1 = toption1.get()
        option2 = toption2.get()
        option3= toption3.get()
        option4=toption4.get()
        answer=tanswer.get()
        
        global mycursor
        global mydb
        
        
        if question!="":
            sql="UPDATE quiz SET question=%s WHERE q_id=%s"
            data=(question,qid)
            mycursor.execute(sql,data)
            mydb.commit()
            if mycursor.rowcount>0:
                messagebox.showinfo("Update Message","Successfully update",parent=updateq)
            else:
                messagebox.showerror("Error","Question Not Updated",parent=updateq)
        if option1!="":
            sql="UPDATE quiz SET option_1=%s WHERE q_id=%s"
            data=(option1,qid)
            mycursor.execute(sql,data)
            mydb.commit()
            if mycursor.rowcount>0:
                messagebox.showinfo("Update Message","Successfully update",parent=updateq)
            else:
                messagebox.showerror("Error","Question Not Updated",parent=updateq)
        if option2!="":
            sql="UPDATE quiz SET option_2=%s WHERE q_id=%s"
            data=(option2,qid)
            mycursor.execute(sql,data)
            mydb.commit()
            if mycursor.rowcount>0:
                messagebox.showinfo("Update Message","Successfully update",parent=updateq)
            else:
                messagebox.showerror("Error","Question Not Updated",parent=updateq)
        if option3!="":
            sql="UPDATE quiz SET option_3=%s WHERE q_id=%s"
            data=(option3,qid)
            mycursor.execute(sql,data)
            mydb.commit()
            if mycursor.rowcount>0:
                messagebox.showinfo("Update Message","Successfully update",parent=updateq)
            else:
                messagebox.showerror("Error","Question Not Updated",parent=updateq)
        if option4!="":
            sql="UPDATE quiz SET option_4=%s WHERE q_id=%s"
            data=(option4,qid)
            mycursor.execute(sql,data)
            mydb.commit()
            if mycursor.rowcount>0:
                messagebox.showinfo("Update Message","Successfully update",parent=updateq)
            else:
                messagebox.showerror("Error","Question Not Updated",parent=updateq)
        if answer!="":
            sql="UPDATE quiz SET answer=%s WHERE q_id=%s"
            data=(answer,qid)
            mycursor.execute(sql,data)
            mydb.commit()
            if mycursor.rowcount>0:
                messagebox.showinfo("Update Message","Successfully update",parent=updateq)
            else:
                messagebox.showerror("Error","Question Not Updated",parent=updateq)
    #Updates BUTTON
    update = Button(updateq_frame,text='Update',padx=5,pady=5,width=5,command =updatequestionToDataBase,bg='green')
    update.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    update.place(relx=0.2,rely=0.9)
    
    def backhome():
        global admin_flag
        admin_flag=2
        admin_menu()
    #back
    back = Button(updateq_frame,text='Back',padx=5,pady=5,width=5,bg="green",command=backhome)
    back.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    back.place(relx=0.6,rely=0.9)

    updateq.mainloop()
#delete Question
def deletequestion():
    ad_menu.destroy()
    global deleteq
    deleteq = Tk()
    
    
    deleteq_canvas = Canvas(deleteq,width=720,height=440,bg="blue")
    deleteq_canvas.pack()

    deleteq_frame = Frame(deleteq_canvas,bg="white")
    deleteq_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(deleteq_frame,text="Delete Question",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #question  id
    idlabel = Label(deleteq_frame,text="Question id ",fg='black',bg='white')
    idlabel.place(relx=0.19,rely=0.4)
    tqid = Entry(deleteq_frame,bg='#d3d3d3',fg='black')
    tqid.config(width=42)
    tqid.place(relx=0.31,rely=0.4)
    def delete():
        qid=tqid.get()
        global mycursor
        global mydb
        sql="DELETE  FROM quiz WHERE q_id=%s"
        data=(str(qid),)
        mycursor.execute(sql,data)
        mydb.commit()
        if mycursor.rowcount>0:
            messagebox.showinfo("Delete Message","Successfully Deleted",parent=daleteq)
        else:
            messagebox.showerror("Error","Question Not Deleted",parent=deleteq)
    #delete    
    log = Button(deleteq_frame,text='Delete',padx=5,pady=5,width=5,command=delete)
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.2,rely=0.6)
    
    def backhome():
        global admin_flag
        admin_flag=3
        admin_menu()
    #back
    back = Button(deleteq_frame,text='Back',padx=5,pady=5,width=5,command=backhome)
    back.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    back.place(relx=0.5,rely=0.6)
    
    deleteq.mainloop()
#Display Question
def displayquestion():
    ad_menu.destroy()
    global m
    m = Tk()
    
    med_canvas = Canvas(m,width=720,height=440,bg="#101357")
    med_canvas.pack()

    med_frame = Frame(med_canvas,bg="white")
    med_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    
    global x
    x=0
    sql="SELECT * FROM quiz"
    mycursor.execute(sql)

    record=mycursor.fetchall()
    count=mycursor.rowcount
    
    ques = Label(med_frame,text =str(record[x][0])+"."+record[x][1],font="calibri 12",bg="white",)
    ques.place(relx=0.1,rely=0.2,)

    a = Label(med_frame,text="a."+record[x][2],font="calibri 10",bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Label(med_frame,text="b."+record[x][3],font="calibri 10",bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Label(med_frame,text="c."+record[x][4],font="calibri 10",bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Label(med_frame,text="d."+record[x][5],font="calibri 10",bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER)
    
    e = Label(med_frame,text="Answer:"+record[x][6],font="calibri 10",bg="white")
    e.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    x=x+1
    
    
    def display(x):
        if x == count:
            nextQuestion.configure(text='End',command=calc)                
        else:
            ques.configure(text =str(record[x][0])+"."+record[x][1])
            
            a.configure(text="a."+record[x][2])
      
            b.configure(text="b."+record[x][3])
      
            c.configure(text="c."+record[x][4])
      
            d.configure(text="d."+record[x][5])
            
            e.configure(text="Answer:"+record[x][6])
            
    def calc():
        global x
        x=x-1
        display(x)
    
    #pre button
    submit = Button(med_frame,command=calc,text="Pre")
    submit.place(relx=0.2,rely=0.82,anchor=CENTER)
     
    def dis():
        global x
        x=x+1
        display(x)
    
    #Next button
    nextQuestion = Button(med_frame,command=dis,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    def backhome():
        global admin_flag
        admin_flag=4
        admin_menu()
    #back button
    back = Button(med_frame,text='Back',padx=5,pady=5,width=5,command=backhome)
    back.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    back.place(relx=0.7,rely=0.1)
    m.mainloop()

#view mark admin
def viewmark():
    ad_menu.destroy()
    global v
    v = Tk()
    
    view_canvas = Canvas(v,width=720,height=440,bg="#101357")
    view_canvas.pack()

    view_frame = Frame(view_canvas,bg="white")
    view_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    sql="SELECT * FROM student_result"
    mycursor.execute(sql)
    record=mycursor.fetchall()
    
    heading = Label(view_frame,text="Result",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.39,rely=0.1)
    
    rollno = Label(view_frame,text ="Roll No",font="calibri 12",bg="white")
    rollno.place(relx=0.2,rely=0.3)
    
    date = Label(view_frame,text ="Date",font="calibri 12",bg="white")
    date.place(relx=0.5,rely=0.3)
    
    mark = Label(view_frame,text ="Mark",font="calibri 12",bg="white")
    mark.place(relx=0.8,rely=0.3)
    x=0.3
    for i in record:
        x=x+0.1
        vrollno= Label(view_frame,text =i[1],font="calibri 12",bg="white")
        vrollno.place(relx=0.2,rely=x)
    
        vdate = Label(view_frame,text =i[3],font="calibri 12",bg="white")
        vdate.place(relx=0.5,rely=x)
    
        vmark = Label(view_frame,text =i[2],font="calibri 12",bg="white")
        vmark.place(relx=0.8,rely=x)
    def backhome():
        global admin_flag
        admin_flag=5
        admin_menu()    
    back = Button(view_frame,text='Back',padx=5,pady=5,width=5,command=backhome)
    back.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    back.place(relx=0.7,rely=0.1)
    v.mainloop()    
#admin menu
def admin_menu():
    if admin_flag==1:
        addq.destroy()
    elif admin_flag==2:
        updateq.destroy()
    elif admin_flag==3:
        deleteq.destroy()
    elif admin_flag==4:
        m.destroy()
    elif admin_flag==5:
        v.destroy()
    else:    
        login.destroy()
    global ad_menu
    ad_menu = Tk()
    ad_canvas = Canvas(ad_menu,width=720,height=440,bg="blue")
    ad_canvas.pack()
    
    ad_frame = Frame(ad_canvas,bg="white")
    ad_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    heading = Label(ad_frame,text="Welcome Admin ",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)
    
        #add question
    add_question = Button(ad_frame,text='ADD QUESTION',padx=5,pady=5,width=5,command=addquestion)
    add_question.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    add_question.place(relx=0.4,rely=0.3)
    
        #update question
    update_question = Button(ad_frame,text='UPDATE QUESTION',padx=5,pady=5,width=5,command=updatequestion)
    update_question.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    update_question.place(relx=0.4,rely=0.4)
    
        #delete question
    delete_question = Button(ad_frame,text='DELETE QUESTION',padx=5,pady=5,width=5,command=deletequestion)
    delete_question.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    delete_question.place(relx=0.4,rely=0.5)    
    
        #display question
    display_question = Button(ad_frame,text='DISPLAY QUESTION',padx=5,pady=5,width=5,command=displayquestion)
    display_question.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    display_question.place(relx=0.4,rely=0.6)
        
    
        #view result
    view_result = Button(ad_frame,text='VIEW RESULT',padx=5,pady=5,width=5,command=viewmark)
    view_result.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    view_result.place(relx=0.4,rely=0.7)
    def logoutpage():
        global flag1
        flag1=1
        signUpPage()
        #logout
    logout = Button(ad_frame,text='LOGOUT',padx=5,pady=5,width=5,command=logoutpage)
    logout.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    logout.place(relx=0.4,rely=0.8)    
    
    ad_menu.mainloop


#<--------------------------------------------------Candidate------------------------------------------------------->
#attmpt quiz    
def attmptquiz(rollno):
    stud_menu.destroy()
    global m
    m = Tk()
    
    med_canvas = Canvas(m,width=720,height=440,bg="#101357")
    med_canvas.pack()

    med_frame = Frame(med_canvas,bg="white")
    med_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    sql="SELECT * FROM quiz"
    answer=[]   
    mycursor.execute(sql)

    record=mycursor.fetchall()
    count=mycursor.rowcount
    #print(count)    
    li=[""]
    for i in range(0,count):
        li.append(i)
    #print(li)    
    #print(record[1][1])
    for i in record: 
        answer.append(i[6])
    #print(answer)    
    index=1
    x = random.choice(li[1:])
    
    ques = Label(med_frame,text =str(index)+"."+record[x][1],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(med_frame,text=record[x][2],font="calibri 10",value=record[x][2],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(med_frame,text=record[x][3],font="calibri 10",value=record[x][3],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(med_frame,text=record[x][4],font="calibri 10",value=record[x][4],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(med_frame,text=record[x][5],font="calibri 10",value=record[x][5],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(m)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        global index
        if len(li) == 1:
                m.destroy()
                showMark(score,rollno)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            index=index+1
            x = random.choice(li[1:])
            ques.configure(text =str(index)+"."+record[x][1])
            
            a.configure(text=record[x][2],value=record[x][2])
      
            b.configure(text=record[x][3],value=record[x][3])
      
            c.configure(text=record[x][4],value=record[x][4])
      
            d.configure(text=record[x][5],value=record[x][5])
            
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(med_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(med_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    m.mainloop()



def showMark(mark,rollno):
    current_time = datetime.datetime.now()
    global sh
    
    sh = Tk()
    
    show_canvas = Canvas(sh,width=720,height=440,bg="#101357")
    show_canvas.pack()

    show_frame = Frame(show_canvas,bg="white")
    show_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    st = "Your score is "+str(mark)
    mlabel = Label(show_canvas,text=st,fg="black",font="calibri 20")
    mlabel.place(relx=0.5,rely=0.2,anchor=CENTER)
    
    da=str(current_time.day)+"/"+str(current_time.month)+"/"+str(current_time.year)        
    sql="INSERT INTO student_result(roll_no,mark,Date)VALUES(%s,%s,%s)"
    data=(rollno,str(mark),da)
    mycursor.execute(sql,data)
    mydb.commit()
    
    def backhome():
        global student_flag
        student_flag=1
        student_menu(rollno)
        
    back = Button(show_frame,text='Back',padx=5,pady=5,width=5,command=backhome)
    back.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    back.place(relx=0.7,rely=0.8)
    
    sh.mainloop()    


#Student View Marks
def viewmark_student(rollno):
    stud_menu.destroy()
    global v
    global mycursor
    global mydb
    v = Tk()
    
    view_canvas = Canvas(v,width=720,height=440,bg="#101357")
    view_canvas.pack()

    view_frame = Frame(view_canvas,bg="white")
    view_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    sql="SELECT * FROM student_result WHERE roll_no=%s"
    data=(rollno,)
    mycursor.execute(sql,data)
    record=mycursor.fetchall()
    
    heading = Label(view_frame,text="Result",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.39,rely=0.1)
    
    rollno = Label(view_frame,text ="Roll No",font="calibri 12",bg="white")
    rollno.place(relx=0.2,rely=0.3)
    
    date = Label(view_frame,text ="Date",font="calibri 12",bg="white")
    date.place(relx=0.5,rely=0.3)
    
    mark = Label(view_frame,text ="Mark",font="calibri 12",bg="white")
    mark.place(relx=0.8,rely=0.3)
    x=0.3
    for i in record:
        x=x+0.1
        vrollno= Label(view_frame,text =i[1],font="calibri 12",bg="white")
        vrollno.place(relx=0.2,rely=x)
    
        vdate = Label(view_frame,text =i[3],font="calibri 12",bg="white")
        vdate.place(relx=0.5,rely=x)
    
        vmark = Label(view_frame,text =i[2],font="calibri 12",bg="white")
        vmark.place(relx=0.8,rely=x)
    
    def backhome():
        global student_flag
        student_flag=2
        student_menu(rollno)
    
    #Back Button    
    back = Button(view_frame,text='Back',padx=5,pady=5,width=5,command=backhome)
    back.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    back.place(relx=0.7,rely=0.8)
    v.mainloop()

#change Password
def changepassword(rollno):
    stud_menu.destroy()
    global change
    change = Tk()
    
    
    change_canvas = Canvas(change,width=720,height=440,bg="blue")
    change_canvas.pack()

    change_frame = Frame(change_canvas,bg="white")
    change_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(change_frame,text="Change Password",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #email id
    ulabel = Label(change_frame,text="Email ",fg='black',bg='white')
    ulabel.place(relx=0.21,rely=0.4)
    email = Entry(change_frame,bg='#d3d3d3',fg='black')
    email.config(width=42)
    email.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(change_frame,text="New Password",fg='black',bg='white')
    plabel.place(relx=0.1,rely=0.5)
    pas = Entry(change_frame,bg='#d3d3d3',fg='black')
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)
    
    def cha_pass():
        username=email.get()
        password=pas.get()
        global mycursor
        global mydb
        sql="UPDATE student SET password=%s WHERE email=%s"
        data=(password,username)
        mycursor.execute(sql,data)
        mydb.commit()
        if mycursor.rowcount>0:
            messagebox.showinfo("confirm Message","Successfully change password",parent=change)
        else:
            messagebox.showerror("Error","Password Not Updated",parent=change)
    
    #submit button
    log = Button(change_frame,text='Submit',padx=5,pady=5,width=5,command=cha_pass)
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.2,rely=0.6)
    
    def backhome():
        global student_flag
        student_flag=3
        student_menu(rollno)
    
    #back button    
    back = Button(change_frame,text='Back',padx=5,pady=5,width=5,command=backhome)
    back.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    back.place(relx=0.5,rely=0.6)
    
    
    change.mainloop()

#student Dashborad/menu
def student_menu(rollno):
    if student_flag==0:
        login.destroy()
    if student_flag==1:
        sh.destroy()
    if student_flag==2:
        v.destroy()
    if student_flag==3:
        change.destroy()
    global stud_menu
    stud_menu = Tk()
    stu_canvas = Canvas(stud_menu,width=720,height=440,bg="blue")
    stu_canvas.pack()
    
    stu_frame = Frame(stu_canvas,bg="white")
    stu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    heading = Label(stu_frame,text="Welcome Quiz App",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)
    
    def quiz():
        attmptquiz(rollno)
    
    #attempt exam
    attempt = Button(stu_frame,text='ATTEMPT EXAM',padx=5,pady=5,width=5,command=quiz)
    attempt.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    attempt.place(relx=0.4,rely=0.4)
    
    def viewmark():
        viewmark_student(rollno)
    
    #view result
    result = Button(stu_frame,text='VIEW RESULT',padx=5,pady=5,width=5,command=viewmark)
    result.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    result.place(relx=0.4,rely=0.5)
    def change_password():
        changepassword(rollno)
    
    #change password
    change_pas = Button(stu_frame,text='CHANGE PASSWORD',padx=5,pady=5,width=5,command=change_password)
    change_pas.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    change_pas.place(relx=0.4,rely=0.6)    

    #logout page
    def logoutpage():
        global flag
        flag=1
        signUpPage()    
    
    #LOGIN BUTTON
    log = Button(stu_frame,text='Logout',padx=5,pady=5,width=5,command=logoutpage)
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.7)

    stud_menu.mainloop()    
#<----------------------------------------login page----------------------------------------------------->

#login Page
def loginPage(logdata):
    
    sup.destroy()
    
    
    global login
    login = Tk()
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width=720,height=440,bg="blue")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="white")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Quiz App Login",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="Username",fg='black',bg='white')
    ulabel.place(relx=0.21,rely=0.4)
    uname = Entry(login_frame,bg='#d3d3d3',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="Password",fg='black',bg='white')
    plabel.place(relx=0.215,rely=0.5)
    pas = Entry(login_frame,bg='#d3d3d3',fg='black',show="*",textvariable = password)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)

    def check():
        for a,b,c,d,e in logdata:
            if d == uname.get() and e == pas.get():
                student_menu(b)
                break
        if uname.get()=="admin" and pas.get()=="admin":
            admin_menu()
            
        else:
            error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check)
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
        
    login.mainloop()

#Signup page
def signUpPage():
    global flag
    global flag1
    if flag==1:
        global stud_menu
        stud_menu.destroy()
    elif flag1==1:
        global ad_menu
        ad_menu.destroy()
    else:
        root.destroy()
    global sup
    sup = Tk()
    
    rollno = StringVar()
    name = StringVar()
    email = StringVar()
    passw = StringVar()
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="blue")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="white")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="Quiz App SignUp",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #Roll no
    rlabel = Label(sup_frame,text="Roll No",fg='black',bg='white')
    rlabel.place(relx=0.21,rely=0.4)
    trollno = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable =rollno)
    trollno.config(width=42)
    trollno.place(relx=0.31,rely=0.4)

    #Name
    nlabel = Label(sup_frame,text="Name",fg='black',bg='white')
    nlabel.place(relx=0.21,rely=0.5)
    tname = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = name)
    tname.config(width=42)
    tname.place(relx=0.31,rely=0.5)
    
    
    #email id
    elabel = Label(sup_frame,text="Email Id",fg='black',bg='white')
    elabel.place(relx=0.215,rely=0.6)
    temail = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable =email)
    temail.config(width=42)
    temail.place(relx=0.31,rely=0.6)
    
    
    
    #password
    plabel = Label(sup_frame,text="Password",fg='black',bg='white')
    plabel.place(relx=0.215,rely=0.7)
    tpas = Entry(sup_frame,bg='#d3d3d3',fg='black',show="*",textvariable = passw)
    tpas.config(width=42)
    tpas.place(relx=0.31,rely=0.7)
    def addUserToDataBase():
        
        rollno = trollno.get()
        name = tname.get()
        email = temail.get()
        pas = tpas.get()
        
        global mycursor
        global mydb
        sql="INSERT INTO student(roll_no,name,email,password)VALUES(%s,%s,%s,%s)"
        data=(rollno,name,email,pas)
        mycursor.execute(sql,data)
        mydb.commit()
        
        sql="SELECT * FROM student"
        mycursor.execute(sql)
        z=mycursor.fetchall()
        
        print(z)       
        loginPage(z)
    def gotoLogin():
        global mycursor
        global mydb
        
        sql="SELECT * FROM student"
        mycursor.execute(sql)
        z=mycursor.fetchall()
        loginPage(z)
    
    #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase,bg='green')
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="white",fg='blue')
    log.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.9)

    sup.mainloop()

def start():
    global root 
    root = Tk()
    canvas = Canvas(root,width = 720,height = 440)
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="back.png")
    canvas.create_image(50,10,image=img,anchor=NW)

    button = Button(root, text='Start',command = signUpPage) 
    button.configure(width = 102,height=2, activebackground = "#33B5E5", bg ='green', relief = RAISED)
    button.grid(column = 0 , row = 2)

    root.mainloop()
    
    
if __name__=='__main__':
    start()
mycursor.close()
mydb.close()

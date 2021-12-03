from tkinter import *
import time
import mysql.connector as sql
from tkinter import messagebox
import sys
sys.path.insert(0,'./assets')

results = []
results2 = []

with open('assets/dbp.txt','r') as pwdt:
    pwd = pwdt.read()
    pwdt.close()

try:
    conn=sql.connect(host='localhost',user='root',passwd=pwd,database='employees',charset='utf8')
    mycursor = conn.cursor()
    
except Exception as e:
    print("Error : ",e)

def register():
    def reg():
        v_em_no = int(entry_1_1.get())
        v_em_name = entry_1_2.get()
        v_em_dept = entry_1_3.get()
        v_em_salary = int(entry_1_4.get())
        v_em_age = int(entry_1_5.get())
        v_sql_insert="insert into office values("+str(v_em_no)+",'" +v_em_name+"','"+v_em_dept+"',"+str(v_em_salary)+","+str(v_em_age)+")"
        mycursor.execute(v_sql_insert)
        conn.commit()
        root_1.destroy()
    root_1 = Tk()
    root_1.title("Employee Registration")
    head_1=Label(root_1,text = "Fill Details to register Employee",font=('Helvetica',10,'bold')).grid(row=0)
    text_1_1 = Label(root_1,text = "Employee ID : ").grid(row=1,sticky = E)
    text_1_2 = Label(root_1,text = "Name : ").grid(row=2,sticky = E)
    text_1_3 = Label(root_1,text = "Department : ").grid(row=3,sticky = E)
    text_1_4 = Label(root_1,text = "Salary : ").grid(row=4,sticky = E)
    text_1_5 = Label(root_1,text = "Age : ").grid(row=5,sticky = E)
    entry_1_1 = Entry(root_1,width = 45)
    entry_1_2 = Entry(root_1,width = 45)
    entry_1_3 = Entry(root_1,width = 45)
    entry_1_4 = Entry(root_1,width = 45)
    entry_1_5 = Entry(root_1,width = 45)
    entry_1_1.grid(row=1,column=1,sticky=W)
    entry_1_2.grid(row=2,column=1,sticky=W)
    entry_1_3.grid(row=3,column=1,sticky=W)
    entry_1_4.grid(row=4,column=1,sticky=W)
    entry_1_5.grid(row=5,column=1,sticky=W)
    text_1_6 = Label(root_1,text="make sure employee id,salary and age are integer").grid(row=6)
    button_1_1 = Button(root_1,text= "Register", fg='blue',command = reg).grid(row=7,column=1)
    root_1.mainloop()
                
def details():
    global results
    class Table:
        def __init__(self,root_2):
            global results
            for i in range(l):
                for j in range(5):
                    exec(f"self.e{i}_{j} = Entry(root_2,width=20,fg='blue',font=('Arial',16,'bold'))")
                    exec(f"self.e{i}_{j}.grid(row={i}+2,column={j})")
                    exec("self.e"+str(i)+"_"+str(j)+".insert(END, results["+str(i)+"]["+str(j)+"])")
        def get(self):
            rlist = []
            for i in range(l):
                jlist = []
                for j in range(5):
                    exec(f"jlist.append(self.e{i}_{j}.get())")
                rlist.append(jlist)
            return rlist
    mycursor.execute("select* from OFFICE")
    results=mycursor.fetchall()
    conn.commit()
    def getr():
        res = t.get()
        mycursor.execute("delete from OFFICE")
        conn.commit()
        for r in res:
            v_em_no = int(r[0])
            v_em_name = r[1]
            v_em_dept = r[2]
            v_em_salary = int(r[3])
            v_em_age = int(r[4])
            v_sql_insert="insert into office values("+str(v_em_no)+",'" +v_em_name+"','"+v_em_dept+"',"+str(v_em_salary)+","+str(v_em_age)+")"
            mycursor.execute(v_sql_insert)
            conn.commit()            

    l = len(results)
    
    root_2 = Tk()
    root_2.title('Details')
    text = Label(root_2,text = "EMPLOYEE DETAILS", font=('Atial',18,'bold')).grid(row=0,column=2)
    text = Label(root_2,text = "ID", font=('Atial',16,'bold')).grid(row=1,column=0,sticky=W)
    text = Label(root_2,text = "Name", font=('Atial',16,'bold')).grid(row=1,column=1,sticky=W)
    text = Label(root_2,text = "Department", font=('Atial',16,'bold')).grid(row=1,column=2,sticky=W)
    text = Label(root_2,text = "Salary", font=('Atial',16,'bold')).grid(row=1,column=3,sticky=W)
    text = Label(root_2,text = "Age", font=('Atial',16,'bold')).grid(row=1,column=4,sticky=W)
    t = Table(root_2)
    b= Button(root_2,text="Update",fg='blue',command = getr).grid(row=l+3,column=4)
    root_2.mainloop()
    

            
    '''
    for x in results:
        str_ = str_ + str(x) +' \n'
    root_2=Tk()
    root_2.withdraw()
    messagebox.showinfo("User Details",str_)
    root_2.destroy()'''
    
def salary_u():
    def inc():
        nam = entry_3_1.get()
        mycursor.execute("update office set em_salary=em_salary+em_salary*10/100 where em_no='{}'".format(nam))
        conn.commit()
        root_3.destroy()
        
    root_3 = Tk()
    root_3.title('Increment')
    head_3 = Label(root_3,text="Select employee to increment salary by 10%",font=('Helvetica',10,'bold')).grid(row=0)
    text_3_1 = Label(root_3,text = "Employee ID : ").grid(row=1,sticky = E)
    entry_3_1 = Entry(root_3)
    entry_3_1.grid(row=1,column=1,sticky=W)
    button_3_1 = Button(root_3,text = "Increment",fg='blue',command=inc).grid(row=2,column=1)
    root_3.mainloop()

def emp_list():
    class Table:
        def __init__(self,root_4):
            for i in range(l):
                self.e = Entry(root_4,width=20,fg='blue',font=("Arial",16,'bold'))
                self.e.grid(row=i+1)
                self.e.insert(END, list_[i])
    mycursor.execute("select em_name from office order by em_name asc")
    list_=mycursor.fetchall()
    l=len(list_)
    '''
    for x in list_:
        str_ = str_ +str(x) +' \n'  '''

    root_4 = Tk()
    root_4.title('Employee List')
    text = Label(root_4,text=f"total no of employee is : {l}").grid(row=0)
    Table(root_4)
    root_4.mainloop()


def emp_no():
    str_=''
    mycursor.execute("select count(distinct em_name) from office")
    count=mycursor.fetchall()
    for x in count:
        str_ = str_ + str(x)
    conn.commit()
    root_5 = Tk()
    root_5.withdraw()
    messagebox.showinfo("No. of Employee",'Total no of employee is : '+str_)
    root_5.destroy()

def performence():
    def pef_inp():
        v_em_no = entry_6_1.get()
        v_em_dept = entry_6_3.get()
        v_em_performance = entry_6_4.get()
        v_em_work = entry_6_5.get()
        v_sql_insert="insert into em_performance values("+v_em_no+",'"+v_em_dept+"','"+v_em_performance+"','"+v_em_work+"')"
        mycursor.execute(v_sql_insert)
        conn.commit()
        root_6.destroy()
        

        
    root_6 = Tk()
    root_6.title('Employee Experience')

    head_6 = Label(root_6,text = "Enter Experience Details of Employees",font=('Helvetica',10,'bold')).grid(row=0)
    text_6_1 = Label(root_6,text = "Employee ID : ").grid(row=1,sticky=E)
    text_6_3 = Label(root_6,text = "Department : ").grid(row=3,sticky=E)
    text_6_4 = Label(root_6,text = "Performence : ").grid(row=4,sticky=E)
    text_6_5 = Label(root_6,text = "Exoerience (years) : ").grid(row=5,sticky=E)
    entry_6_1 = Entry(root_6,width = 45)
    entry_6_3 = Entry(root_6,width = 45)
    entry_6_4 = Entry(root_6,width = 45)
    entry_6_5 = Entry(root_6,width = 45)
    entry_6_1.grid(row=1,column=1,sticky=W)
    entry_6_3.grid(row=3,column=1,sticky=W)
    entry_6_4.grid(row=4,column=1,sticky=W)
    entry_6_5.grid(row=5,column=1,sticky=W)
    button_6_1 = Button(root_6,text = "Confirm",fg='blue',command=pef_inp).grid(row=6,column=1)

    root_6.mainloop()

def salary():
    def sal():
        str_=''
        em_no = entry_7_1.get()
        a=mycursor.execute("select em_salary from office where em_no='{}'".format(em_no))
        mycursor.execute(a)
        salary=mycursor.fetchall()
        for x in salary:
            str_ += str(x)
        conn.commit()
        root_7.destroy()
        root_8=Tk()
        root_8.withdraw()
        messagebox.showinfo("Salary of Employee",'Salary of Employee No '+em_no+' is : '+str_)
        root_8.destroy()
        
        
    root_7 = Tk()
    root_7.title('Salary')
    head_7 = Label(root_7,text="Enter Employee ID to know salary",font=('Helvetica',10,'bold')).grid(row=0)
    text_7_1 = Label(root_7,text = "Employee ID : ").grid(row=1,sticky=W)
    entry_7_1 = Entry(root_7)
    entry_7_1.grid(row=1,column=1,sticky=E)
    button_7_1 = Button(root_7,text = "Confirm", fg="blue",command=sal).grid(row=2,column=1)

def we():
    global results2
    class Table:
        def __init__(self,root_8):
            for i in range(l):
                for j in range(4):
                    exec(f"self.e{i}_{j} = Entry(root_8,width=20,fg='blue',font=('Arial',16,'bold'))")
                    exec(f"self.e{i}_{j}.grid(row={i}+2,column={j})")
                    exec("self.e"+str(i)+"_"+str(j)+".insert(END, results2["+str(i)+"]["+str(j)+"])")
        def get(self):
            rlist = []
            for i in range(l):
                jlist = []
                for j in range(4):
                    exec(f"jlist.append(self.e{i}_{j}.get())")
                rlist.append(jlist)
            return rlist

    def upd():
        res = t2.get()
        mycursor.execute("delete from em_performance")
        conn.commit()
        for r in res:
            v_em_no = r[0]
            v_em_dept = r[1]
            v_em_performance = r[2]
            v_em_work = r[3]
            v_sql_insert="insert into em_performance values("+v_em_no+",'"+v_em_dept+"','"+v_em_performance+"','"+v_em_work+"')"
            mycursor.execute(v_sql_insert)
            conn.commit()

    mycursor.execute("select* from em_performance")
    results2=mycursor.fetchall()
    conn.commit()

    l = len(results2)
    
    root_8 = Tk()
    root_8.title('Details')
    text = Label(root_8,text = "EMPLOYEE DETAILS", font=('Atial',18,'bold')).grid(row=0,column=2)
    text = Label(root_8,text = "ID", font=('Atial',16,'bold')).grid(row=1,column=0,sticky=W)
    text = Label(root_8,text = "Department", font=('Atial',16,'bold')).grid(row=1,column=1,sticky=W)
    text = Label(root_8,text = "Performance", font=('Atial',16,'bold')).grid(row=1,column=2,sticky=W)
    text = Label(root_8,text = "Experience(years)", font=('Atial',16,'bold')).grid(row=1,column=3,sticky=W)
    t2 = Table(root_8)
    b= Button(root_8,text = "Update", fg='blue', command = upd).grid(row=l+3,column=3)
    root_8.mainloop()

def fire():
    def fr():
        em = entry_9.get()
        st = f"delete from office where em_no = {em}"
        try:
            mycursor.execute(st)
            conn.commit()
        except:
            pass
        st2 = f"delete from em_performance where em_no = {em}"
        try:
            mycursor.execute(st2)
            conn.commit()
        except:
            pass
        root_9.destroy()
            
    
    root_9 = Tk()
    root_9.title('FIRE EMPLOYEE')
    head = Label(root_9,text = 'FIRE EMPLOYEE',font=('Helvetica',10,'bold')).grid(row=0)
    text = Label(root_9,text = "Enter Employee Number : ").grid(row=1,sticky=W)
    entry_9 = Entry(root_9)
    entry_9.grid(row=1,column=1,sticky=E)
    button = Button(root_9,text="FIRE",fg='blue',command=fr).grid(row=2,column=1)
    

def menu():
    root = Tk()
    root.title('Home')
    root.geometry("265x280")
    head = Label(root,text = " EMPLOYEES MANAGEMENT SYSTEM ",font=('Helvetica',10,'bold')).grid(row=0)
    text_1 = Label(root,text = "Select the task to be Performed").grid(row=1)
    button_1 = Button(root,text='Employee Registration',fg='blue',width=20,command=register).grid(row=2)
    button_2 = Button(root,text='    Employee Details    ',fg='blue',width=20,command=details).grid(row=3)
    button_3 = Button(root,text=' Increment Salary  10%',fg='blue',width=20,command=salary_u).grid(row=4)
    button_4 = Button(root,text='      Employees List      ',fg='blue',width=20,command=emp_list).grid(row=5)
    button_5 = Button(root,text=' Total No. of Emoloyee',fg='blue',width=20,command=emp_no).grid(row=6,)
    button_6 = Button(root,text='     Work Experience    ',fg='blue',width=20,command=performence).grid(row=7)
    button_7 = Button(root,text='    Know your Salary    ',fg='blue',width=20,command=salary).grid(row=8)
    button_8 = Button(root,text='Display Work experience ',fg='blue',width=20,command=we).grid(row=9)
    button_9 = Button(root,text='FIRE EMPLOYEE',fg='blue',width=20,command=fire).grid(row=10)
    root.mainloop()

menu()

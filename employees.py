from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
import pymysql
from tkinter import messagebox  # Required for messagebox.showinfo()


def connect_database():
    try:
        # Establish the connection to MySQL server
        connection = pymysql.connect(
            host='localhost',
            user='root',
            passwd='Aditya@321',
            charset='utf8'
        )
        cursor = connection.cursor()

        return cursor,connection  # Return the connection object for further use

    except pymysql.Error as e:
        messagebox.showinfo('Error', f"Database connection error: {e}")
        return None, None  # Indicate failure


def create_database_table():
    cursor,connection = connect_database()

    # Create database if not exists and switch to it
    cursor.execute('CREATE DATABASE IF NOT EXISTS inventory_system')
    cursor.execute('USE inventory_system')

    # Create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS employee_data (
        emp_id INT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        gender VARCHAR(50),
        dob VARCHAR(30),
        contact VARCHAR(30),
        employment_type VARCHAR(50),
        education VARCHAR(50),
        work_shift VARCHAR(50),
        address VARCHAR(100),
        doj VARCHAR(30),
        salary VARCHAR(50),
        usertype VARCHAR(50),
        password VARCHAR(50)
    )''')

    connection.commit()  # Ensure changes are saved

def select_user_data(event,emp_id_entry,name_entry,email_entry,gender_combobox,dob_entry,contact_entry,employment_type_combobox,education_combobox,work_shift_type_combobox,address_entry,doj_entry,salary_entry,usertype_combobox,password_entry):
    index = employee_treeview.selection()
    content = employee_treeview.item(index)
    row = content['values']
    clear_fields(emp_id_entry,name_entry,email_entry,gender_combobox,dob_entry,contact_entry,employment_type_combobox,education_combobox,work_shift_type_combobox,address_entry,doj_entry,salary_entry,usertype_combobox,password_entry,False)
    emp_id_entry.insert(0,row[0])
    name_entry.insert(0,row[1])
    email_entry.insert(0,row[2])
    gender_combobox.set(row[3])
    dob_entry.set_date(row[4])
    contact_entry.insert(0,row[5])
    employment_type_combobox.set(row[6])
    education_combobox.set(row[7])
    work_shift_type_combobox.set(row[8])
    address_entry.insert(1.0,row[9])
    doj_entry.set_date(row[10])
    salary_entry.insert(0,row[11])
    usertype_combobox.set(row[12])
    password_entry.insert(0,row[13])


def add_user(emp_id,name,email,gender,dob,contact,employment_type,education,work_shift,address,doj,salary,usertype,password):
    if (emp_id == '' or name=='' or email=='' or gender=='Select Gender' or contact=='' or employment_type=='Select Type' or education=='Select Education' or work_shift=='Select Work Shift' or address=='\n' or salary=='' or usertype=='Select User Type' or password=='') :
        messagebox.showerror('Error', 'Please enter all required fields.')
    else:
        cursor,connection = connect_database()
        if not cursor or not connection:
            return
        cursor.execute('USE inventory_system')
        try:
            cursor.execute('SELECT emp_id from employee_data WHERE emp_id=%s',(emp_id,))
            if cursor.fetchone():
                messagebox.showerror('Error', 'Employee ID already exists.')
                return
            address=address.strip()
            cursor.execute('INSERT INTO employee_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(emp_id,name,email,gender,dob,contact,employment_type,education,work_shift,address,doj,salary,usertype,password))
            connection.commit()
            treeview_data()
            messagebox.showinfo('Success', 'User added successfully.')
        except pymysql.Error as e:
            messagebox.showerror('Error', f"Database connection error: {e}")
        finally:
            cursor.close()
            connection.close()


def treeview_data():
    cursor,connection = connect_database()
    if not cursor or not connection:
        return
    cursor.execute('use inventory_system')
    try:
        cursor.execute('SELECT * FROM employee_data')
        user_records = cursor.fetchall()
        employee_treeview.delete(*employee_treeview.get_children())
        for record in user_records:
            employee_treeview.insert('',END,values=record)
    except pymysql.Error as e:
        messagebox.showinfo('Error', f"Database connection error: {e}")
    finally:
        cursor.close()
        connection.close()

def clear_fields(emp_id_entry,name_entry,email_entry,gender_combobox,dob_entry,contact_entry,employment_type_combobox,education_combobox,work_shift_type_combobox,address_entry,doj_entry,salary_entry,usertype_combobox,password_entry,check):
    emp_id_entry.delete(0,END)
    name_entry.delete(0,END)
    email_entry.delete(0,END)
    gender_combobox.set(value="Select Gender")
    from datetime import date
    dob_entry.set_date(date.today())
    contact_entry.delete(0,END)
    employment_type_combobox.set(value="Select Type")
    education_combobox.set(value="Select Education")
    work_shift_type_combobox.set(value="Select Work Shift")
    address_entry.delete(1.0,END)
    doj_entry.set_date(date.today())
    salary_entry.delete(0,END)
    usertype_combobox.set(value="Select User Type")
    password_entry.delete(0,END)
    if check:
        employee_treeview.selection_remove(employee_treeview.selection())

def update_user(emp_id,name,email,gender,dob,contact,employment_type,education,work_shift,address,doj,salary,usertype,password):
    selected = employee_treeview.selection()
    if not selected:
        messagebox.showerror('Error', 'Please select an employee to edit.')
    else:
        cursor,connection = connect_database()
        if not cursor or not connection:
            return
        try:
            cursor.execute('use inventory_system')
            cursor.execute('SELECT * FROM employee_data WHERE emp_id=%s',(emp_id,))
            current_data=cursor.fetchone()
            current_data=current_data[1:]
            print(current_data)
            address=address.strip()
            new_data=(name,email,gender,dob,contact,employment_type,education,work_shift,address,doj,salary,usertype,password)
            print(new_data)
            if current_data==new_data:
                messagebox.showinfo('Information', 'No Changes Detected.')
                return
            cursor.execute('UPDATE employee_data SET name=%s,email=%s,gender=%s, dob=%s,contact=%s, employment_type=%s,education=%s,work_shift=%s,address=%s,doj=%s,salary=%s,usertype=%s,password=%s WHERE emp_id=%s',(name,email,gender,dob,contact,employment_type,education,work_shift,address,doj,salary,usertype,password,emp_id))
            connection.commit()
            messagebox.showinfo('Success', 'User updated successfully.')
            treeview_data()
        except pymysql.Error as e:
            messagebox.showerror('Error', f"Database connection error: {e}")
        finally:
            cursor.close()
            connection.close()


def delete_user(emp_id,name):
    selected = employee_treeview.selection()
    if not selected:
        messagebox.showerror('Error', 'Please select an employee to Delete.')
    else:
        result = messagebox.askyesno('Confirm', 'Do You Really want to Delete %s?' % name)
        if result:
            cursor, connection = connect_database()
            if not cursor or not connection:
                return
            try:
                cursor.execute('use inventory_system')
                cursor.execute('DELETE FROM employee_data WHERE emp_id=%s',(emp_id,))
                connection.commit()
                treeview_data()
                messagebox.showinfo('Success', 'User deleted successfully.')
            except pymysql.Error as e:
                messagebox.showerror('Error', f"Database connection error: {e}")

            finally:
                cursor.close()
                connection.close()

def search_user(search_option,value):
    if search_option=='Search By':
        messagebox.showerror('Error', 'No Option is Selected.')
    elif value=='':
        messagebox.showerror('Error', 'Enter a value to search.')
    else:
        cursor, connection = connect_database()
        if not cursor or not connection:
            return
        try:
            cursor.execute('use inventory_system')
            cursor.execute(f'SELECT * FROM employee_data WHERE {search_option.lower()} LIKE %s',f'%{value.lower()}%')
            records=cursor.fetchall()
            employee_treeview.delete(*employee_treeview.get_children())
            for record in records:
                employee_treeview.insert('',END,values=record)
        except pymysql.Error as e:
            messagebox.showerror('Error', f"Database connection error: {e}")
        finally:
            cursor.close()
            connection.close()
        # print(search_option,value)




def employee_form(window):
    global back_image,employee_treeview
    employee_frame = Frame(window,width=1070,height=567,bg="white")
    employee_frame.place(x=200,y=100)
    heading_label = Label(employee_frame,text="Manage Employee Details", font=("times new roman", 16,'bold'),bg="#0f4d7d",fg="white")
    heading_label.place(x=0,y=0,relwidth=1)
    back_image = PhotoImage(file="images/back.png")
    back_button=Button(employee_frame,image=back_image,bd=0,cursor="hand2",bg='white',command= lambda:employee_frame.place_forget())
    back_button.place(x=10,y=30)
    # Parent Top Frame --------------------------
    top_frame = Frame(employee_frame,bg="white")
    top_frame.place(x=0, y= 60, relwidth=1, height=235)
    # Child 1st
    search_frame = Frame(top_frame,bg="white")
    search_frame.pack()
    search_combobox=ttk.Combobox(search_frame, values=('Emp_ID','Name','Email'),font=('times new roman', 12),state='readonly',justify=CENTER)
    search_combobox.set(value="Search By")
    search_combobox.grid(row=0,column=0,padx=20)
    search_entry = Entry(search_frame,font=('times new roman', 12),bg='lightyellow')
    search_entry.grid(row=0,column=1,padx=20)
    search_button = Button(search_frame,text="Search",font=('times new roman', 12),bg='#0f4d7d',width=10,cursor="hand2",fg='white',command=lambda:search_user(search_combobox.get(),search_entry.get()))
    search_button.grid(row=0,column=2,padx=20)
    show_all_button = Button(search_frame,text="Show All",font=('times new roman', 12),bg='#0f4d7d',width=10,cursor="hand2",fg='white',command=show_all(search_combobox,search_entry))
    show_all_button.grid(row=0,column=3,padx=20)
    # Child 2nd
    horizontal_scrollbar = Scrollbar(top_frame,orient=HORIZONTAL)
    vertical_scrollbar = Scrollbar(top_frame,orient=VERTICAL)
    employee_treeview = ttk.Treeview(top_frame,columns=('emp_id','name','email','gender','dob','contact','employment_type','education','work_shift','address','doj','salary','usertype'),
                                     show='headings',yscrollcommand=vertical_scrollbar,xscrollcommand=horizontal_scrollbar)

    horizontal_scrollbar.pack(side=BOTTOM,fill=X)
    vertical_scrollbar.pack(side=RIGHT,fill=Y)
    horizontal_scrollbar.config(command=employee_treeview.xview)
    vertical_scrollbar.config(command=employee_treeview.yview)

    employee_treeview.pack(pady=(10,0))
    employee_treeview.heading('emp_id',text='Employee ID')
    employee_treeview.heading('name',text='Name')
    employee_treeview.heading('email',text='Email')
    employee_treeview.heading('gender',text='Gender')
    employee_treeview.heading('dob',text='Date of Birth')
    employee_treeview.heading('contact',text='Contact')
    employee_treeview.heading('employment_type',text='Employee Type')
    employee_treeview.heading('education',text='Education')
    employee_treeview.heading('work_shift',text='Work Shift')
    employee_treeview.heading('address',text='Address')
    employee_treeview.heading('doj',text='Date of Joining')
    employee_treeview.heading('salary',text='Salary')
    employee_treeview.heading('usertype',text='User Type')

    employee_treeview.column('emp_id',width=80)
    employee_treeview.column('name',width=140)
    employee_treeview.column('email',width=200)
    employee_treeview.column('gender',width=50)
    employee_treeview.column('dob',width=100)
    employee_treeview.column('contact',width=120)
    employee_treeview.column('employment_type',width=150)
    employee_treeview.column('education',width=120)
    employee_treeview.column('work_shift',width=100)
    employee_treeview.column('address',width=200)
    employee_treeview.column('doj',width=140)
    employee_treeview.column('salary',width=140)
    employee_treeview.column('usertype',width=140)

    treeview_data()


    detail_frame = Frame(employee_frame,bg="white")
    detail_frame.place(x=20,y=300)
    # empl_id
    emp_id_label = Label(detail_frame,text='Employee ID',font=('times new roman',12),bg='White',fg='black')
    emp_id_label.grid(row=0,column=0,padx=20,pady=5,sticky=W)
    emp_id_entry = Entry(detail_frame,font=('times new roman', 12),bg='lightyellow')
    emp_id_entry.grid(row=0,column=1,padx=20,pady=5)
    # name
    name_label = Label(detail_frame,text='Name',font=('times new roman',12),bg='White',fg='black')
    name_label.grid(row=0,column=2,padx=20,pady=5,sticky=W)
    name_entry = Entry(detail_frame,font=('times new roman', 12),bg='lightyellow')
    name_entry.grid(row=0,column=3,padx=20,pady=5)
    # email
    email_label = Label(detail_frame,text='Email',font=('times new roman',12),bg='White',fg='black')
    email_label.grid(row=0,column=4,padx=20,pady=5,sticky=W)
    email_entry = Entry(detail_frame,font=('times new roman', 12),bg='lightyellow')
    email_entry.grid(row=0,column=5,padx=20,pady=5)
    # gender
    gender_label = Label(detail_frame,text='Gender',font=('times new roman',12),bg='White',fg='black')
    gender_label.grid(row=1,column=0,padx=20,pady=5,sticky=W)
    gender_combobox = Combobox(detail_frame,width=24,values=['Male','Female'],state='readonly',justify=CENTER)
    gender_combobox.set(value="Select Gender")
    gender_combobox.grid(row=1,column=1,padx=20,pady=5)
    # dob
    dob_label = Label(detail_frame,text='D.O.B',font=('times new roman',12),bg='White',fg='black')
    dob_label.grid(row=1,column=2,padx=20,pady=5,sticky=W)
    dob_entry = DateEntry(detail_frame,width=18,font=('times new roman', 12),state='readonly',date_pattern='dd/mm/yyy')
    dob_entry.grid(row=1,column=3,padx=20,pady=5)
    # contact
    contact_label = Label(detail_frame,text='Contact No.',font=('times new roman',12),bg='White',fg='black')
    contact_label.grid(row=1,column=4,padx=20,pady=5,sticky=W)
    contact_entry = Entry(detail_frame,font=('times new roman', 12),bg='lightyellow')
    contact_entry.grid(row=1,column=5,padx=20,pady=5)
    # employment_type
    employment_type_label = Label(detail_frame,text='Employment Type',font=('times new roman',12),bg='White',fg='black')
    employment_type_label.grid(row=2,column=0,padx=20,pady=5,sticky=W)
    employment_type_combobox = Combobox(detail_frame,width=24,values=['Full Time','Part Time','Casual','Contract','Intern'],state='readonly',justify=CENTER)
    employment_type_combobox.set(value="Select Type")
    employment_type_combobox.grid(row=2,column=1,padx=20,pady=5)
    # education
    education_label = Label(detail_frame,text='Education',font=('times new roman',12),bg='White',fg='black')
    education_label.grid(row=2,column=2,padx=20,pady=5,sticky=W)
    education_combobox = Combobox(detail_frame,width=24,values=['Graduate','Intermediate','Matric'],state='readonly',justify=CENTER)
    education_combobox.set(value="Select Education")
    education_combobox.grid(row=2,column=3,padx=20,pady=5)
    # work_shift
    work_shift_label = Label(detail_frame,text='Work Shift',font=('times new roman',12),bg='White',fg='black')
    work_shift_label.grid(row=2,column=4,padx=20,pady=5,sticky=W)
    work_shift_type_combobox = Combobox(detail_frame,width=24,values=['Morning','Evening','Night'],state='readonly',justify=CENTER)
    work_shift_type_combobox.set(value="Select Work Shift")
    work_shift_type_combobox.grid(row=2,column=5,padx=20,pady=5)
    # address
    address_label = Label(detail_frame,text='Address',font=('times new roman',12),bg='White',fg='black')
    address_label.grid(row=3,column=0,padx=20,pady=5,sticky=W)
    address_entry = Text(detail_frame,width=20,height=3,font=('times new roman', 12),bg='lightyellow')
    address_entry.grid(row=3,column=1)
    # doj
    doj_label = Label(detail_frame,text='Date of Joining',font=('times new roman',12),bg='White',fg='black')
    doj_label.grid(row=3,column=2,padx=20,pady=5,sticky=W)
    doj_entry = DateEntry(detail_frame,width=18,font=('times new roman', 12),state='readonly',date_pattern='dd/mm/yyy')
    doj_entry.grid(row=3,column=3,padx=20,pady=5)
    # user_type
    usertype_label = Label(detail_frame,text='User Type',font=('times new roman',12),bg='White',fg='black')
    usertype_label.grid(row=3,column=4,padx=20,pady=5,sticky=W)
    usertype_combobox = Combobox(detail_frame,width=24,values=['Admin','Employee'],state='readonly',justify=CENTER)
    usertype_combobox.set(value="Select User Type")
    usertype_combobox.grid(row=3,column=5,padx=20,pady=5)
    # salary
    salary_label = Label(detail_frame,text='Salary',font=('times new roman',12),bg='White',fg='black')
    salary_label .grid(row=4,column=2,padx=20,pady=5,sticky=W)
    salary_entry = Entry(detail_frame,font=('times new roman', 12),bg='lightyellow')
    salary_entry.grid(row=4,column=3,padx=20,pady=5)
    # password
    password_label = Label(detail_frame,text='Password',font=('times new roman',12),bg='White',fg='black')
    password_label .grid(row=4,column=4,padx=20,pady=5,sticky=W)
    password_entry = Entry(detail_frame,font=('times new roman', 12),bg='lightyellow')
    password_entry.grid(row=4,column=5,padx=20,pady=5)
    # Buttons To Save , Update, Delete, Clear
    button_frame = Frame(employee_frame,bg="white")
    button_frame.place(x=200,y=515)
    add_user_button = Button(button_frame, text="Save", font=('times new roman', 12), bg='#0f4d7d', width=10,
                           cursor="hand2", fg='white',command= lambda :add_user(emp_id_entry.get(),name_entry.get(),email_entry.get(),gender_combobox.get(),dob_entry.get(),contact_entry.get(),employment_type_combobox.get(),education_combobox.get(),work_shift_type_combobox.get(),address_entry.get("1.0", "end-1c"),doj_entry.get(),salary_entry.get(),usertype_combobox.get(),password_entry.get()))
    add_user_button.grid(row=0, column=0, padx=20)
    update_user_button = Button(button_frame, text="Update", font=('times new roman', 12), bg='#0f4d7d', width=10,
                           cursor="hand2", fg='white',command=lambda :update_user(emp_id_entry.get(),name_entry.get(),email_entry.get(),gender_combobox.get(),dob_entry.get(),contact_entry.get(),employment_type_combobox.get(),education_combobox.get(),work_shift_type_combobox.get(),address_entry.get("1.0", "end-1c"),doj_entry.get(),salary_entry.get(),usertype_combobox.get(),password_entry.get()))
    update_user_button.grid(row=0, column=1, padx=20)
    delete_user_button = Button(button_frame, text="Delete", font=('times new roman', 12), bg='#0f4d7d', width=10,
                           cursor="hand2", fg='white',command= lambda :delete_user(emp_id_entry.get(),name_entry.get()))
    delete_user_button.grid(row=0, column=2, padx=20)
    clear_user_button = Button(button_frame, text="Clear", font=('times new roman', 12), bg='#0f4d7d', width=10,
                           cursor="hand2", fg='white',command= lambda :clear_fields(emp_id_entry,name_entry,email_entry,gender_combobox,dob_entry,contact_entry,employment_type_combobox,education_combobox,work_shift_type_combobox,address_entry,doj_entry,salary_entry,usertype_combobox,password_entry,True))
    clear_user_button.grid(row=0, column=3, padx=20)
    employee_treeview.bind('<ButtonRelease-1>',lambda event:select_user_data(event,emp_id_entry,name_entry,email_entry,gender_combobox,dob_entry,contact_entry,employment_type_combobox,education_combobox,work_shift_type_combobox,address_entry,doj_entry,salary_entry,usertype_combobox,password_entry))
    create_database_table()

def show_all(search_combobox,search_entry):
    pass
    # treeview_data()
    # search_entry.delete(0,END)
    # search_combobox.set('Search By')



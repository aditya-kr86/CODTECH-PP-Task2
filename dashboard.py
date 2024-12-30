from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from employees import employee_form
import pymysql


# GUI Part
window = Tk()
window.geometry('1270x668+0+0')
window.title('Inventory Management System')
# window.resizable(False, False)
window.config(background='white')

# --------------------------------------------------------------------------Tittle---------------------------------------------------------------------------
icon_image = PhotoImage(file='images/icon.png')
titleLabel = Label(window,image=icon_image,compound=LEFT, text='\tInventory Management System\t',font=('times new roman', 40,'bold'),bg='#010c48',fg='white',anchor='w',padx=0)
titleLabel.place(x=0,y=0,relwidth=1)

logoutButton = Button(window, text='Logout',font=('times new roman',20,'bold'),fg='#010c48')
logoutButton.place(x=1100,y=10)

# ---------------------------------------------------------- Welcome with Date and Time --------------------------------------------------------------
subtitleLabel = Label(window, text='Welcome Admin\t\t Date: 27-12-2024\t\t Time: 12:36:17 pm',font=('times new roman',15,'bold'),bg='#4d636d',fg='white')
subtitleLabel.place(x=0,y=70,relwidth=1)

# --------------------------------------------------------------------------Left Frame---------------------------------------------------------------------------
leftFrame = Frame(window)
leftFrame.place(x=0,y=102,width=200,height=555)

logoImage = PhotoImage(file='images/logo.png')
imageLabel = Label(leftFrame,image=logoImage)
imageLabel.grid(row=0,column=0)
imageLabel.pack()

menuLabel = Label(leftFrame,text='Menu',font=('times new roman',20),bg='#009688')
menuLabel.pack(fill=X)

employee_icon = PhotoImage(file='images/employee.png')
employee_button = Button(leftFrame,image=employee_icon,compound=LEFT, text='  Employee',font=('times new roman',20,'bold'),anchor='w',padx=10,command= lambda:employee_form(window))
employee_button.pack(fill=X)

supplier_icon = PhotoImage(file='images/supplier.png')
supplier_button = Button(leftFrame, image=supplier_icon,compound=LEFT, text='  Supplier',font=('times new roman',20,'bold'),anchor='w',padx=10)
supplier_button.pack(fill=X)

cat_icon = PhotoImage(file='images/category.png')
cat_button = Button(leftFrame,image=cat_icon,compound=LEFT, text='  Category',font=('times new roman',20,'bold'),anchor='w',padx=10)
cat_button.pack(fill=X)

product_icon = PhotoImage(file='images/product.png')
product_button = Button(leftFrame, image=product_icon, compound=LEFT, text='  Product',font=('times new roman',20,'bold'),anchor='w',padx=10)
product_button.pack(fill=X)

sales_icon = PhotoImage(file='sales.png')
sales_button = Button(leftFrame, text='  Sales', font=('times new roman', 20, 'bold'), anchor='w', padx=10)
sales_button.pack(fill=X)


exit_icon = PhotoImage(file='images/exit.png')
exit_button = Button(leftFrame, image=exit_icon, compound=LEFT, text='  Exit',font=('times new roman',20,'bold'),anchor='w',padx=10)
exit_button.pack(fill=X)

#--------------------------------------------------------------------------Middle Frame Frame---------------------------------------------------------------------------
### Employees Frame
emp_frame = Frame(window,bg='#2C3E50',bd=3,relief=RIDGE)
emp_frame.place(x=400,y=125,height=170,width=280)
total_emp_icon = PhotoImage(file='images/total_emp.png')
total_emp_icon_label = Label(emp_frame,image=total_emp_icon,bg='#2C3E50')
total_emp_icon_label.pack()

total_emp_label = Label(emp_frame,text='Total Employees',font=('times new roman',15,'bold'),bg='#2C3E50',fg='white')
total_emp_label.pack()
total_emp_count_label= Label(emp_frame,text='0',font=('times new roman',30,'bold'),bg='#2C3E50',fg='white')
total_emp_count_label.pack()

### Suppliers Frame
sup_frame = Frame(window,bg='#8C42AC',bd=3,relief=RIDGE)
sup_frame.place(x=750,y=125,height=170,width=280)
total_sup_icon = PhotoImage(file='images/total_sup.png')
total_sup_icon_label = Label(sup_frame,image=total_sup_icon,bg='#8C42AC')
total_sup_icon_label.pack()

total_sup_label = Label(sup_frame,text='Total Suppliers',font=('times new roman',15,'bold'),bg='#8C42AC',fg='white')
total_sup_label.pack()
total_sup_count_label= Label(sup_frame,text='0',font=('times new roman',30,'bold'),bg='#8C42AC',fg='white')
total_sup_count_label.pack()

### cat Frame
cat_frame = Frame(window,bg='#26AD5E',bd=3,relief=RIDGE)
cat_frame.place(x=400,y=310,height=170,width=280)
total_cat_icon = PhotoImage(file='images/total_cat.png')
total_cat_icon_label = Label(cat_frame,image=total_cat_icon,bg='#26AD5E')
total_cat_icon_label.pack()

total_cat_label = Label(cat_frame,text='Total Categories',font=('times new roman',15,'bold'),bg='#26AD5E',fg='white')
total_cat_label.pack()
total_cat_count_label= Label(cat_frame,text='0',font=('times new roman',30,'bold'),bg='#26AD5E',fg='white')
total_cat_count_label.pack()

### prod Frame
prod_frame = Frame(window,bg='#2780B9',bd=3,relief=RIDGE)
prod_frame.place(x=750,y=310,height=170,width=280)
total_prod_icon = PhotoImage(file='images/total_prod.png')
total_prod_icon_label = Label(prod_frame,image=total_prod_icon,bg='#2780B9')
total_prod_icon_label.pack()

total_prod_label = Label(prod_frame,text='Total Products',font=('times new roman',15,'bold'),bg='#2780B9',fg='white')
total_prod_label.pack()
total_prod_count_label= Label(prod_frame,text='0',font=('times new roman',30,'bold'),bg='#2780B9',fg='white')
total_prod_count_label.pack()

### Sales Frame
sales_frame = Frame(window,bg='#BE3E31',bd=3,relief=RIDGE)
sales_frame.place(x=625,y=495,height=170,width=280)
sales_icon = PhotoImage(file='images/total_sales.png')
sales_icon_label = Label(sales_frame,image=sales_icon,bg='#BE3E31')
sales_icon_label.pack()

sales_label = Label(sales_frame,text='Total Sales',font=('times new roman',15,'bold'),bg='#BE3E31',fg='white')
sales_label.pack()
sales_count_label= Label(sales_frame,text='0',font=('times new roman',30,'bold'),bg='#BE3E31',fg='white')
sales_count_label.pack()















window.mainloop()

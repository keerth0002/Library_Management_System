import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

import mysql.connector
from tkinter import messagebox
import datetime
import tkinter




# Main Application Class
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")



        #----------------------------------------variable-------------------------

        self.member_var=tk.StringVar()
        self.prn_Var=tk.StringVar()
        self.id_Var=tk.StringVar()
        self.firstname_Var=tk.StringVar()
        self.lastname_Var=tk.StringVar()
        self.address1_Var=tk.StringVar()
        self.address2_Var=tk.StringVar()
        self.postcode_Var=tk.StringVar()
        self.mobile_Var=tk.StringVar()
        self.bookid_Var=tk.StringVar()
        self.booktitle_Var=tk.StringVar()
        self.author_Var=tk.StringVar()
        self.databorrowed_Var=tk.StringVar()
        self.datedue_Var=tk.StringVar()
        self.daysonbooks_Var=tk.StringVar()
        self.latereturnfine_Var=tk.StringVar()
        self.dateoverdue_Var=tk.StringVar()
        self.finalprice_Var=tk.StringVar()


        # Main Frame
        lbltitle = tk.Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg= "lightcoral",fg="blue",bd=20,relief="ridge",font=("times new roman",50,"bold"), padx=2, pady=6)
        lbltitle.pack(side=tk.TOP,fill=tk.X)

        frame=tk.Frame(self.root,bd=12,relief=tk.RIDGE,padx=20,bg="pink")
        frame.place(x=0,y=130,width=1530,height=400)

        #---------------------------------DataFrameLeft----------------------------------

        DataframeLeft=tk.LabelFrame(frame,text="Library Membership Information",bg="blue",fg="lightblue",bd=20,relief="ridge",font=("times new roman",13,"bold"))
        DataframeLeft.place(x=0,y=5,width=900,height=350)


        lblMember=tk.Label(DataframeLeft,bg="blue",text="Member Type",foreground="white",font=("arial",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=tk.W)

        comMember =ttk.Combobox(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.member_var,width=29,state="readonly")
        comMember["value"]=("admin Staf","Student","Lecturer")
        comMember.grid(row=0,column=1)
        #PRN 

        lblPRN_No=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="PRN NO:",padx=2,pady=6,fg="white",bg="blue")
        lblPRN_No.grid(row=1,column=0,sticky=tk.W)
        txtPRN_NO=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.prn_Var,width=29)
        txtPRN_NO.grid(row=1,column=1)

       
        #Title

        lblTitle=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="ID NO:",padx=2,pady=6,fg="white",bg="blue")
        lblTitle.grid(row=2,column=0,sticky=tk.W)
        txtTitle=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.id_Var,width=29)
        txtTitle.grid(row=2,column=1)

        #FirstName
        lblFirstName=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="FIRST NAME:",padx=2,pady=6,fg="white",bg="blue")
        lblFirstName.grid(row=3,column=0,sticky=tk.W)
        txtFirstName=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.firstname_Var,width=29)
        txtFirstName.grid(row=3,column=1)

        #LastName
        lblLastName=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="LAST NAME:",padx=2,pady=6,fg="white",bg="blue")
        lblLastName.grid(row=4,column=0,sticky=tk.W)
        txtLastName=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.lastname_Var,width=29)
        txtLastName.grid(row=4,column=1)

        #Address1
        lblAddress1=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="ADDRESS 1:",padx=2,pady=6,fg="white",bg="blue")
        lblAddress1.grid(row=5,column=0,sticky=tk.W)
        txtAddress1=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.address1_Var,width=29)
        txtAddress1.grid(row=5,column=1)


        #Address2
        lblAddress2=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="ADDRESS 2:",padx=2,pady=6,fg="white",bg="blue")
        lblAddress2.grid(row=6,column=0,sticky=tk.W)
        txtAddress2=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.address2_Var,width=29)
        txtAddress2.grid(row=6,column=1)


        #PostCode
        lblPostCode=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="POSTCODE:",padx=2,pady=6,fg="white",bg="blue")
        lblPostCode.grid(row=7,column=0,sticky=tk.W)
        txtPostCode=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.postcode_Var,width=29)
        txtPostCode.grid(row=7,column=1)

        #Mobile
        lblMobile=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="MOBILE NO.:",padx=2,pady=6,fg="white",bg="blue")
        lblMobile.grid(row=8,column=0,sticky=tk.W)
        txtMobile=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.mobile_Var,width=29)
        txtMobile.grid(row=8,column=1)

        #BookId
        lblBookId=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="BOOK ID:",padx=2,pady=6,fg="white",bg="blue")
        lblBookId.grid(row=0,column=2,sticky=tk.W)
        txtBookId=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.bookid_Var,width=29)
        txtBookId.grid(row=0,column=3)

        #BookTitle
        lblBookTitle=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="BOOK TITLe:",padx=2,pady=6,fg="white",bg="blue")
        lblBookTitle.grid(row=1,column=2,sticky=tk.W)
        txtBookTitle=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.booktitle_Var,width=29)
        txtBookTitle.grid(row=1,column=3)
        
        #Author
        lblAuthor=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="AUTHOR NAME:",padx=2,pady=6,fg="white",bg="blue")
        lblAuthor.grid(row=2,column=2,sticky=tk.W)
        txtAuthor=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.author_Var,width=29)
        txtAuthor.grid(row=2,column=3)


        #DateBorrowed
        lblDateBorrowed=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="DATE BORROWED:",padx=2,pady=6,fg="white",bg="blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=tk.W)
        txtDateBorrowed=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.databorrowed_Var,width=29)
        txtDateBorrowed.grid(row=3,column=3)


        #Duedate
        lblDuedate=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="DUE DATE:",padx=2,pady=6,fg="white",bg="blue")
        lblDuedate.grid(row=4,column=2,sticky=tk.W)
        txtDuedate=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.datedue_Var,width=29)
        txtDuedate.grid(row=4,column=3)



        #DaysonBooks
        lblDaysonBooks=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="DAYS ON BOOKS:",padx=2,pady=6,fg="white",bg="blue")
        lblDaysonBooks.grid(row=5,column=2,sticky=tk.W)
        txtDaysonBooks=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.daysonbooks_Var,width=29)
        txtDaysonBooks.grid(row=5,column=3)


        #LateResturnFine
        lblLateResturnFine=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="LAST RETURN FINE:",padx=2,pady=6,fg="white",bg="blue")
        lblLateResturnFine.grid(row=6,column=2,sticky=tk.W)
        txtLateResturnFine=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.latereturnfine_Var,width=29)
        txtLateResturnFine.grid(row=6,column=3)



        #DateOverDate
        lblDateOverDate=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="DATE-OVER DATE:",padx=2,pady=6,fg="white",bg="blue")
        lblDateOverDate.grid(row=7,column=2,sticky=tk.W)
        txtDateOverDate=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.dateoverdue_Var,width=29)
        txtDateOverDate.grid(row=7,column=3)


        #ActualPrice
        lblActualPrice=tk.Label(DataframeLeft,font=("arial",12,"bold"),text="ACTUAL PRICE",padx=2,pady=6,fg="white",bg="blue")
        lblActualPrice.grid(row=8,column=2,sticky=tk.W)
        txtActualPrice=tk.Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.finalprice_Var,width=29)
        txtActualPrice.grid(row=8,column=3)


        #--------------------------------DataFrameRight-------------------------------------------------


        DataframeRight=tk.LabelFrame(frame,text="Book Details",bg="blue",fg="lightblue",bd=20,relief="ridge",font=("times new roman",12,"bold"))
        DataframeRight.place(x=910,y=5,width=540,height=350)

        self.txtBox= tk.Text(DataframeRight, font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar=tk.Scrollbar(DataframeRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=["Robotics in practice","Architects of Intelligence","Rise of the Robots","Computational Intelligence in Robotics and Automation","Techniques and Applications","Industrial Automation and Robotics","Artificial Intelligence: A Modern Approach", "Robotics for Programmers" ,"Programming in C", "Introduction to Machine Learning", 
                    "Robotics: Modelling, Planning and Control" "C Programming Language", "Machine Learning: A Probabilistic Perspective", 
                    "Introduction to Autonomous Robots", "C Programming: A Modern Approach", "Deep Learning", "Probabilistic Robotics", 
                    "The Art of C Programming", "Pattern Recognition and Machine Learning", "Robotics: Control, Sensing, Vision, and Intelligence"]


        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if(x=="Robotics in practice"):
                self.bookid_Var.set("BKID1001")
                self.booktitle_Var.set("Robotics in practice")
                self.author_Var.set("Joseph F. Engelberge")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_Var.set(d1)
                self.datedue_Var.set(d3)
                
                self.daysonbooks_Var.set(15)
                self.latereturnfine_Var.set("Rs.20")
                self.dateoverdue_Var.set("NO")
                self.finalprice_Var.set("Rs.150")

            elif(x=="Rise of the Robots"):
                self.bookid_Var.set("BKID1003")
                self.booktitle_Var.set("Rise of the Robots")
                self.author_Var.set("Martin Ford")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_Var.set(d1)
                self.datedue_Var.set(d3)
                
                self.daysonbooks_Var.set(15)
                self.latereturnfine_Var.set("Rs.30")
                self.dateoverdue_Var.set("NO")
                self.finalprice_Var.set("Rs.150")

            elif(x=="Architects of Intelligence"):
                self.bookid_Var.set("BKID1002")
                self.booktitle_Var.set("Architects of Intelligence")
                self.author_Var.set("Martin Ford")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_Var.set(d1)
                self.datedue_Var.set(d3)
                
                self.daysonbooks_Var.set(15)
                self.latereturnfine_Var.set("Rs.30")
                self.dateoverdue_Var.set("NO")
                self.finalprice_Var.set("Rs.150")




        listBox=tk.Listbox(DataframeRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(tk.END,item)


        #-------------------------------buttons-------------------------------------------

        framebutton=tk.Frame(self.root,bd=12,relief="ridge",padx=20,bg="pink")
        framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=tk.Button(framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0, column=0)

        btnAddData=tk.Button(framebutton,command=self.show_data,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0, column=1)

        btnAddData=tk.Button(framebutton,command=self.update_date,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData=tk.Button(framebutton,command=self.delete_data,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0, column=3)

        btnAddData=tk.Button(framebutton,command=self.reset_data,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData=tk.Button(framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0, column=5)

       

        #----------------------------------information frame------------------------


        frameDetails=tk.Frame(self.root,bd=12,relief="ridge",padx=20,bg="pink")
        frameDetails.place(x=0,y=590,width=1530,height=210)

        Table_frame=tk.Frame(frameDetails,bd=6,relief="ridge",padx=20,bg="lightcoral")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        self.library_table=ttk.Treeview(Table_frame,columns=("membertype","prono","title","firstname","lastname","address1",
                                        "address2","postcode","mobile","bookid","booktitle",
                                        "author","DateBorrowed","Duedate","Days","lateReturnFine",
                                        "DateOverDate","finalprice"))
        xscroll=tk.Scrollbar(frameDetails)
       
        yscroll=tk.Scrollbar(frameDetails)


        #listScrollbar=tk.Scrollbar(DataframeRight)
        #listScrollbar.grid(row=0,column=1,sticky="ns")

        
        """v_scrollbar = ttk.Scrollbar(root, orient='vertical', command=frameDetails.xview)

        h_scrollbar = ttk.Scrollbar(root, orient='horizontal', command=frameDetails.yview)

        frameDetails.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        self.library_table.grid(row=0, column=0, sticky='nsew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar.grid(row=1, column=0, sticky='ew')"""
        
        xscroll.pack(side=tk.BOTTOM,fill=tk.X)
        yscroll.pack(side=tk.RIGHT,fill=tk.Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prono",text="PRN No")
        self.library_table.heading("title",text="Id No")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postcode",text="Post-Id")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book-Id")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("DateBorrowed",text="Date Borrowed")
        self.library_table.heading("Duedate",text="Due-Date")
        self.library_table.heading("Days",text="Days on Books")
        self.library_table.heading("lateReturnFine",text="Late-Return Fine")
        self.library_table.heading("DateOverDate",text="Date-Over Date")
        self.library_table.heading("finalprice",text="Final-Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill="both",expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prono",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postcode",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("DateBorrowed",width=100)
        self.library_table.column("Duedate",width=100)
        self.library_table.column("Days",width=100)
        self.library_table.column("lateReturnFine",width=100)
        self.library_table.column("DateOverDate",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root", password="Mysql@02",database="library_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                          (self.member_var.get(),
                          self.prn_Var.get(),
                          self.id_Var.get(),
                          self.firstname_Var.get(),
                          self.lastname_Var.get(),
                          self.address1_Var.get(),
                          self.address2_Var.get(),
                          self.postcode_Var.get(),
                          self.mobile_Var.get(),
                          self.bookid_Var.get(),
                          self.booktitle_Var.get(),
                          self.author_Var.get(),
                          self.databorrowed_Var.get(),
                          self.datedue_Var.get(),
                          self.daysonbooks_Var.get(),
                          self.latereturnfine_Var.get(),
                          self.dateoverdue_Var.get(),
                          self.finalprice_Var.get(),))
        

        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success","Member Has Been Inserted Sucessfully")
    
    
    def update_date(self):
        conn=mysql.connector.connect(host="localhost",username="root", password="Mysql@02",database="library_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("UPDATE library SET Member=%s, PRN_NO=%s, ID=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, PostID=%s, Mobile=%s, BookID=%s, BookTitle=%s, Author=%s, Date_borrowed=%s, Due_date=%s, Daysofbook=%s, `Late_return_fine`=%s, `Date_over_due`=%s, `Final_price`=%s WHERE ID=%s",
                       
                          (self.member_var.get(),
                           self.prn_Var.get(),
                          self.id_Var.get(),
                          self.firstname_Var.get(),
                          self.lastname_Var.get(),
                          self.address1_Var.get(),
                          self.address2_Var.get(),
                          self.postcode_Var.get(),
                          self.mobile_Var.get(),
                          self.bookid_Var.get(),
                          self.booktitle_Var.get(),
                          self.author_Var.get(),
                          self.databorrowed_Var.get(),
                          self.datedue_Var.get(),
                          self.daysonbooks_Var.get(),
                          self.latereturnfine_Var.get(),
                          self.dateoverdue_Var.get(),
                          self.finalprice_Var.get(),
                          self.id_Var.get(),
                          
                          ))
            
       

        conn.commit()
        self.fatch_data()
        self.reset_data()
        conn.close()

        messagebox.showinfo("Sucess","Data as been Updated")

    
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root", password="Mysql@02",database="library_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",tk.END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        curson_row=self.library_table.focus()
        content=self.library_table.item(curson_row)
        row = content['values']

        self.member_var.set(row[0]),
        self.prn_Var.set(row[1]),
        self.id_Var.set(row[2]),
        self.firstname_Var.set(row[3]),
        self.lastname_Var.set(row[4]),
        self.address1_Var.set(row[5]),
        self.address2_Var.set(row[6]),
        self.postcode_Var.set(row[7]),
        self.mobile_Var.set(row[8]),
        self.bookid_Var.set(row[9]),
        self.booktitle_Var.set(row[10]),
        self.author_Var.set(row[11]),
        self.databorrowed_Var.set(row[12]),
        self.datedue_Var.set(row[13]),
        self.daysonbooks_Var.set(row[14]),
        self.latereturnfine_Var.set(row[15]),
        self.dateoverdue_Var.set(row[16]),
        self.finalprice_Var.set(row[17])

    def  show_data(self):
        self.txtBox.insert(tk.END,"Member Type\t\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(tk.END,"PRN No\t\t\t"+ self.prn_Var.get() + "\n")
        self.txtBox.insert(tk.END,"Title\t\t\t"+ self.id_Var.get() + "\n")
        self.txtBox.insert(tk.END,"First Name\t\t\t"+ self.firstname_Var.get() + "\n")
        self.txtBox.insert(tk.END,"Last Name\t\t\t"+ self.lastname_Var.get() + "\n")
        self.txtBox.insert(tk.END,"Address1\t\t\t"+ self.address1_Var.get() + "\n")
        self.txtBox.insert(tk.END,"Address2\t\t\t"+ self.address2_Var.get() + "\n")
        self.txtBox.insert(tk.END,"Post-Id\t\t\t"+ self.postcode_Var.get() + "\n")
        self.txtBox.insert(tk.END,"Mobile\t\t\t"+ self.mobile_Var.get() + "\n")
        self.txtBox.insert(tk.END,"Book-Id\t\t\t"+ self.bookid_Var.get() + "\n")
        self.txtBox.insert(tk.END,"Book Title\t\t\t"+ self.booktitle_Var.get() + "\n")
        self.txtBox.insert(tk.END,"Author\t\t\t"+ self.author_Var.get() + "\n")
        self.txtBox.insert(tk.END,"Date Borrowed\t\t\t"+ self.databorrowed_Var.get() + "\n")
        self.txtBox.insert(tk.END,"Due-Date\t\t\t"+ self.datedue_Var.get() + "\n")
        self.txtBox.insert(tk.END,"Days on Books\t\t\t"+ self.daysonbooks_Var.get() + "\n")
        self.txtBox.insert(tk.END,"Late-Return Fine\t\t\t"+ self.latereturnfine_Var.get() + "\n")
        self.txtBox.insert(tk.END,"Date-Over Date\t\t\t"+ self.dateoverdue_Var.get() + "\n")
        self.txtBox.insert(tk.END,"Final-Price\t\t\t"+ self.finalprice_Var.get() + "\n")
       
    def reset_data(self):
        self.member_var.set(""),
        self.prn_Var.set(""),
        self.id_Var.set(""),
        self.firstname_Var.set(""),
        self.lastname_Var.set(""),
        self.address1_Var.set(""),
        self.address1_Var.set(""),
        self.address2_Var.set(""),
        self.postcode_Var.set(""),
        self.mobile_Var.set(""),
        self.bookid_Var.set(""),
        self.booktitle_Var.set(""),
        self.author_Var.set(""),
        self.databorrowed_Var.set(""),
        self.datedue_Var.set(""),
        self.daysonbooks_Var.set(""),
        self.latereturnfine_Var.set(""),
        self.dateoverdue_Var.set(""),
        self.finalprice_Var.set(""),
        self.txtBox.delete("1.0",tk.END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System", "Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete_data(self):
        if self.prn_Var.get()=="" or self.id_Var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root", password="Mysql@02",database="library_management_system")
            my_cursor=conn.cursor()
            query="delete from library where PRN_No=%s"
            value=(self.prn_Var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset_data()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")


#-------------------------------------------Main--------------------------------------------------------------

                                 

if __name__ == "__main__":
    root =tk.Tk()
    app = LibraryApp(root)
    root.mainloop()

    
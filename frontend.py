from tkinter import *
import tkinter.messagebox
import backend
class Student:

    def __init__(self,root):
        self.root =root
        self.root.title("Online Movie Ticket Booking System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="orange")

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()
# --------------------------------------FUNCTIONS-------------------------------------------------------------------
        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Database Management Systems", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        def clearData():
            self.txtStdID.delete(0, END)
            self.txtfna.delete(0, END)
            self.txtSna.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAdr.delete(0, END)
            self.txtMobile.delete(0, END)
        def addData():
            if(len(StdID.get())!=0):
                backend.addStdRec(StdID.get(), Firstname.get(), Surname.get() , DoB.get() ,Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))

        def DisplayData():
            studentlist.delete(0,END)
            for row in backend.viewData():
                studentlist.insert(END, row, str(""))

        def StudentRec(event):
            # global sd
            searchStd= studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END, sd[1])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END, sd[2])
            self.txtSna.delete(0, END)
            self.txtSna.insert(END, sd[3])
            self.txtDoB.delete(0, END)
            self.txtDoB.insert(END, sd[4])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, sd[5])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, sd[6])
            self.txtAdr.delete(0, END)
            self.txtAdr.insert(END, sd[7])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, sd[8])

        def DeleteData():
            if(len(StdID.get())!=0):
                backend.deleteRec(StdID.get())
                clearData()
                DisplayData()

        def searchDatabase():
            studentlist.delete(0,END)
            for row in backend.searchData(StdID.get(), Firstname.get(), Surname.get() , DoB.get() ,Age.get(), Gender.get(), Address.get(), Mobile.get()):
                studentlist.insert(END, row, str(""))

        def update():
            if (len(StdID.get()) != 0):
                backend.deleteRec(StdID.get())
            if (len(StdID.get()) != 0):
                backend.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(),Address.get(), Mobile.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))
#--------------------------------------Frames-----------------------------------------------------------------------__________________________________________________________
        MainFrame = Frame(self.root, bg="orange")
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd=2, padx=54,pady=8, bg="orange", relief=RIDGE)
        TitFrame.pack(side=TOP)
        self.lblTit = Label(TitFrame ,font=('Arial',51,'bold'),text="Online Movie Ticket Booking System",bg="orange")
        self.lblTit.grid()
        ButtonFrame =Frame(MainFrame,bd=2,width=1350,height=70,padx=19,pady=10,bg="orange",relief =RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE,bg="orange")
        DataFrame.pack(side=BOTTOM)
        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20,relief=RIDGE,bg="orange", font=('Arial',26,'bold'),text="Movie Info\n")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,bg="orange",font=('Arial',20,'bold'),text="Movie Details\n")
        DataFrameRIGHT.pack(side=RIGHT)
#--------------------------------entries-------------------------------------------------------------------------------------------------
        self.lblStdID = Label(DataFrameLEFT, font=('Arial', 20, 'bold'), text="Movie ID:",padx=2,pady=2,bg="orange")
        self.lblStdID.grid(row=0,column=0,sticky=W)
        self.txtStdID = Entry(DataFrameLEFT, font=('Arial', 20, 'bold'), textvariable=StdID, width=39)
        self.txtStdID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLEFT, font=('Arial', 20, 'bold'), text="Movie Name:", padx=2, pady=2,bg="orange")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('Arial', 20, 'bold'), textvariable=Firstname, width=39)
        self.txtfna.grid(row=1, column=1)

        self.lblSna = Label(DataFrameLEFT, font=('Arial', 20, 'bold'), text="Release Date:", padx=2, pady=2,bg="orange")
        self.lblSna.grid(row=2, column=0, sticky=W)
        self.txtSna = Entry(DataFrameLEFT, font=('Arial', 20, 'bold'), textvariable=Surname, width=39)
        self.txtSna.grid(row=2, column=1)

        self.lblDoB = Label(DataFrameLEFT, font=('Arial', 20, 'bold'), text="Director:", padx=2, pady=2,bg="orange")
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(DataFrameLEFT, font=('Arial', 20, 'bold'), textvariable=DoB, width=39)
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLEFT, font=('Arial', 20, 'bold'), text="Cast:", padx=2, pady=2,bg="orange")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('Arial', 20, 'bold'), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(DataFrameLEFT, font=('Arial', 20, 'bold'), text="Budget:", padx=2, pady=2,bg="orange")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('Arial', 20, 'bold'), textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1)

        self.lblAdr = Label(DataFrameLEFT, font=('Arial', 20, 'bold'), text="Duration:", padx=2, pady=2,bg="orange")
        self.lblAdr.grid(row=6, column=0, sticky=W)
        self.txtAdr = Entry(DataFrameLEFT, font=('Arial', 20, 'bold'), textvariable=Address, width=39)
        self.txtAdr.grid(row=6, column=1)

        self.lblMobile = Label(DataFrameLEFT, font=('Arial', 20, 'bold'), text="Rating:", padx=2, pady=2,bg="orange")
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(DataFrameLEFT, font=('Arial', 20, 'bold'), textvariable=Mobile, width=39)
        self.txtMobile.grid(row=7, column=1)
#--------------------------------------scroll bar and list box----------------------------------------------------------------------------
        scrollbar= Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        studentlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('Arial', 12, 'bold'),yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>',StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=studentlist.yview)
#--------------------------------------buttons-----------------------------------------------------------------------------------------------------------
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('Arial', 20, 'bold'), height=1, width=10, bd=4, command=addData)
        self.btnAddData.grid(row=0, column =0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('Arial', 20, 'bold'), height=1, width=10, bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('Arial', 20, 'bold'), height=1, width=10, bd=4,command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('Arial', 20, 'bold'), height=1, width=10, bd=4,command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('Arial', 20, 'bold'), height=1, width=10, bd=4,command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('Arial', 20, 'bold'), height=1, width=10, bd=4,command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('Arial', 20, 'bold'), height=1, width=10, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)

if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
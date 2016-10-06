
##Julia Neuman
##CS 4400
##902983027/ jneuman18@gatech.edu

##Library DB
from Tkinter import*
import datetime
import tkMessageBox
import pymysql
import time
import unicodedata




class library:

    def __init__(self,win):
        self.win=win
        self.LoginPage(win)

    def LoginPage(self,win):

        self.win=win
        win.title("Login")

        usernameL=Label(win, text = "Username")
        usernameL.grid(row=1, column=0,sticky=W)

        self.username=StringVar()
        usernameE=Entry(win, textvariable=self.username, width=30)
        usernameE.grid(row=1, column=1, columnspan=3)


        passwordL=Label(win, text="Password")
        passwordL.grid(row=2,column=0, sticky=W)

        self.password=StringVar()
        passwordE=Entry(win, textvariable=self.password, width=30)
        passwordE.grid(row=2, column=1, columnspan=3)

        createAccountB=Button(win, text="Create Account", command=self.Register)
        createAccountB.grid(row=3, column=2, sticky=N+E+S+W)

        loginB=Button(win, text="Login", command=self.LoginCheck)
        loginB.grid(row=3, column=3, sticky=N+E+S+W)

        exitB=Button(win, text="Exit", command=self.destroywin)
        exitB.grid(row=3, column=4)

    def Connect(self):

        try:
            db=pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_28", db="cs4400_Group_28", passwd="5d6jPsCn")
            return db
        except:
            tkMessageBox.showerror("Error!","Cannot connect to the database")
            return None


    def LoginCheck(self):
        x=0
        db=self.Connect()
        cursor=db.cursor()

        loginusername=self.username.get()

        loginpassword=self.password.get()

        sql="SELECT Username, Password FROM USER"


        cursor.execute(sql)



        for i in cursor:
            name=loginusername

            dataname=i[0]
            datapass=i[1]
            if dataname==name and datapass==loginpassword:
                x=1
                loggedInUser=name
        if x==1:
            tkMessageBox.showinfo("Successful", "You logged in successfully")
            db.commit()

            db2=self.Connect()
            cursor2=db2.cursor()
            sql2="SELECT StaffUsername FROM STAFF"
            cursor.execute(sql2)

            for i in cursor:
                usernameStaff=i[0]
                if usernameStaff == loggedInUser:
                    x=2
            if x==2:
                self.isStaff="Yes"
                self.staffhomepage()

            if x==1:
                self.isStaff="No"
                self.homepage()

        elif x!=1:
            tkMessageBox.showerror("Error!", "Unrecognizable username/password combination")

        db.commit()




    def homepage(self):
        self.Homepage=Toplevel(self.win)
        self.win.withdraw()
        win = self.Homepage
        win.title("Homepage")


        b1=Button(win, text="Search Books", command=self.searchBooks)
        b1.grid(row=0, column=0, padx=3, pady=3)

        b2=Button(win, text="Request Extension", command=self.requestExtension)
        b2.grid(row=0, column=1, padx=3, pady=3)

        b4=Button(win, text="Track Book Location", command=self.trackBookLocation)
        b4.grid(row=1, column=0, padx=3, pady=3)


        b8=Button(win, text="Future Hold Request", command=self.futureHoldRequest)
        b8.grid(row=1, column=1, padx=3, pady=3)

        b9=Button(win, text="Popular Books Report", command=self.popularBooksReport)
        b9.grid(row=2, column=0, padx=3, pady=3)

        b10=Button(win, text="Frequent Users Report", command=self.frequentUserReport)
        b10.grid(row=2, column=1, padx=3, pady=3)

        b11=Button(win, text="Popular Subjects Report", command=self.popularSubjectReport)
        b11.grid(row=3, column=0, padx=3, pady=3)

        b8=Button(win, text="Damaged Books Report", command=self.damagedBooksReport)
        b8.grid(row=3, column=1, padx=3, pady=3)





    def staffhomepage(self):
        self.StaffHomepage=Toplevel(self.win)
        self.win.withdraw()
        win = self.StaffHomepage
        win.title("Staff Homepage")


        b4=Button(win, text="Track Book Location", command=self.trackBookLocation)
        b4.grid(row=0, column=0, padx=3, pady=3)

        b5=Button(win, text="Checkout a Book", command=self.bookCheckout)
        b5.grid(row=0, column=1, padx=3, pady=3)

        b6=Button(win, text="Return a Book", command=self.returnBook)
        b6.grid(row=1, column=0, padx=3, pady=3)

        b7=Button(win, text="Charge for Lost or Damaged Book", command=self.lostDamagedBook)
        b7.grid(row=1, column=1, padx=3, pady=3)

        b8=Button(win, text="Damaged Books Report", command=self.damagedBooksReport)
        b8.grid(row=2, column=0, padx=3, pady=3)

        b9=Button(win, text="Popular Books Report", command=self.popularBooksReport)
        b9.grid(row=2, column=1, padx=3, pady=3)

        b10=Button(win, text="Frequent Users Report", command=self.frequentUserReport)
        b10.grid(row=3, column=0, padx=3, pady=3)

        b11=Button(win, text="Popular Subjects Report", command=self.popularSubjectReport)
        b11.grid(row=3, column=1, padx=3, pady=3)


    def destroywin(self):
        win.destroy()


    def Register(self):

        self.register=Toplevel(self.win)
        win=self.register

        win.title("New User Registration")

        usernameL=Label(win, text = "Username")
        usernameL.grid(row=1, column=0,sticky=W)

        self.newUsername=StringVar()
        newUsernameE=Entry(win, textvariable=self.newUsername, width=30)
        newUsernameE.grid(row=1
                          , column=1, columnspan=3, sticky=E)


        newPasswordL=Label(win, text="Password")
        newPasswordL.grid(row=2,column=0, sticky=W)

        self.newPassword=StringVar()
        newPasswordE=Entry(win, textvariable=self.newPassword, width=30)
        newPasswordE.grid(row=2, column=1, columnspan=3, sticky=E)

        confirmpasswordL=Label(win, text="Confirm Password")
        confirmpasswordL.grid(row=3,column=0, sticky=W)

        self.confirmpassword2=StringVar()
        confirmpasswordE=Entry(win, textvariable=self.confirmpassword2, width=30)
        confirmpasswordE.grid(row=3, column=1, columnspan=3, sticky=E)

        RegisterB=Button(win, text="Register", command=self.registerCheck)
        RegisterB.grid(row=5, column=3)



        win.lift()

    def registerCheck(self):
        registerusername=self.newUsername.get()
        registerpassword=self.newPassword.get()
        registerconfirmpassword=self.confirmpassword2.get()

        no=2
        if registerpassword==registerconfirmpassword:
            letters=0
        else:
            tkMessageBox.showerror("Error!", "The passwords must match")
            no=1

        if (len(registerusername) ==0):
            tkMessageBox.showerror("Error!", "Please enter a username")
            no=1
        if (len(registerpassword) ==0):
            tkMessageBox.showerror("Error!", "Please enter a password")
            no=1

        if no==2:
            db=self.Connect()
            cursor=db.cursor()

            sql="SELECT Username FROM USER WHERE Username = (%s)"
            cursor.execute(sql, (registerusername))

            for i in cursor:

                no=3
            if no==3:
                tkMessageBox.showerror("Error!", "That username already exists! Please try another!")

            elif no==2:
                sql2 = "INSERT INTO USER (Username, Password) VALUES (%s, %s)"
                cursor.execute(sql2, (registerusername, registerpassword))

                db.commit()
                self.username=registerusername

                self.CreateProfile()











    def CreateProfile(self):

        self.createProfile=Toplevel(self.register)
        self.register.withdraw()
        win = self.createProfile
        win.title("Create Profile")


        firstNameL=Label(win, text = "First Name:")
        firstNameL.grid(row=1, column=1, sticky=W)

        self.firstName=StringVar()
        firstNameE=Entry(win, textvariable=self.firstName, width=30)
        firstNameE.grid(row=1, column=2)

        lastNameL=Label(win, text = "Last Name:")
        lastNameL.grid(row=1, column=3, sticky=W)

        self.lastName=StringVar()
        lastNameE=Entry(win, textvariable=self.lastName, width=30)
        lastNameE.grid(row=1, column=4, columnspan=3, sticky=E)

        dobL=Label(win, text = "D.O.B. (YYYY-MM-DD) :")
        dobL.grid(row=2, column=1, sticky=W)

        self.dob=StringVar()
        dobE=Entry(win, textvariable=self.dob, width=30)
        dobE.grid(row=2, column=2, sticky=W)

        genderL=Label(win, text = "Gender: ")
        genderL.grid(row=2, column=3, sticky=W)

        self.gender=StringVar()

        genderE = OptionMenu(win, self.gender, "M", "F")
        genderE.grid(row=2, column=4, sticky=W)

        emailL=Label(win, text = "Email: ")
        emailL.grid(row=3, column=1, sticky=W)

        self.email=StringVar()
        emailE=Entry(win, textvariable=self.email, width=30)
        emailE.grid(row=3, column=2, sticky=W)

        facultyL=Label(win, text = "Are you a faculty member? ")
        facultyL.grid(row=3, column=3, sticky=W)

        self.faculty=StringVar()
        self.faculty.set("No")

        facultyYesE=Radiobutton(win, text="Yes", value="Yes", variable=self.faculty, command = self.chooseDept)
        facultyYesE.grid(row=3, column=4, sticky=W)


        addressL=Label(win, text = "Address :")
        addressL.grid(row=4, column=1, sticky=W)

        self.address=StringVar()
        addressE=Entry(win, textvariable=self.address, width=30)
        addressE.grid(row=4, column=2, sticky=W)

        asscDeptL=Label(win, text = "Associated Department ")
        asscDeptL.grid(row=4, column=3, sticky=W)

        self.asscDept = StringVar()


        global asscDeptE

        asscDeptE = OptionMenu(win, self.asscDept, "")
        asscDeptE.grid(row=4, column=4, sticky=W)

        submitB=Button(win, text="Submit", command = self.registerUser)
        submitB.grid(row=5, column=4, sticky=E)



    def chooseDept(self):
        win = self.createProfile
        asscDeptE = OptionMenu(win, self.asscDept, "Physics", "Engineering", "Liberal Arts", "Computer Science")
        asscDeptE.grid(row=4, column=4, sticky=W)



    def registerUser(self):
        no=1

        if (len(self.firstName.get())==0 or len(self.lastName.get())==0 or len(self.faculty.get())==0):
            no=2
            tkMessageBox.showerror("Error!", "Please fill in the your first name, last name, and if you are faculty.")


        if (no==1):
            self.fullname=self.firstName.get()+self.lastName.get()

            db=self.Connect()
            cursor=db.cursor()

            sql = "INSERT INTO STUDENTFACULTY (StudentUsername, Name, DOB, Gender, Email, Address, Faculty, Dept) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (self.username, self.fullname, self.dob.get(), self.gender.get(), self.email.get(), self.address.get(), self.faculty.get(), self.asscDept.get()))

            db.commit()
            self.homepage()



    def searchBooks(self):
        self.SearchBooks=Toplevel(self.win)
        win = self.SearchBooks
        win.title("Search Books")

        Label(win, text="ISBN").grid(row=0, column=0, sticky=W)

        self.ISBN=StringVar()
        ISBNE=Entry(win, textvariable=self.ISBN, width=30)
        ISBNE.grid(row=0, column=1,sticky=W)


        Label(win, text="Title").grid(row=1, column=0, sticky=W)

        self.title=StringVar()
        titleE=Entry(win, textvariable=self.title, width=30)
        titleE.grid(row=1, column=1,sticky=W)

        Label(win, text="Author").grid(row=2, column=0, sticky=W)


        self.author=StringVar()
        authorE=Entry(win, textvariable=self.author, width=30)
        authorE.grid(row=2, column=1,sticky=W)

        buttonF=Frame(win)
        buttonF.grid(row=3, column=0, columnspan=2)

        backB=Button(buttonF, text = "Back", command=self.searchBack)
        backB.grid(row=0,column=0)

        searchB=Button(buttonF, text = "Search", command = self.search)
        searchB.grid(row=0, column=1)

        closeB=Button(buttonF, text = "Close", command = self.destroywin)
        closeB.grid(row=0, column=2)

    def destroywinback(self):
        win.destroy()
        self.homepage()

    def search(self):

        ISBN = self.ISBN.get()
        title = self.title.get()
        author = self.author.get()

        liketitle = "%" + title + "%"

        if (len(ISBN)!=0):
            db=self.Connect()
            cursor=db.cursor()

            sql = "SELECT * FROM ((SELECT ISBN, Title, Edition, OnReserve FROM BOOK WHERE ISBN = (%s)) as table1 NATURAL JOIN (SELECT COUNT(CopyNO), CopyISBN as ISBN FROM BOOKCOPY WHERE CopyISBN = (%s) and CheckedOut='No' AND OnHold='No' AND DAMAGED ='No' GROUP BY CopyISBN) as table2)"
            cursor.execute(sql, (ISBN, ISBN))


            self.availBooksList=[]
            self.reserveBooksList=[]
            for i in cursor:
                if i[3] == "No":
                    self.availBooksList.append(i)
                elif i[3] == "Yes":
                    self.reserveBooksList.append(i)


            db.commit()
            self.holdRequest()

        elif (len(title)!=0 and len(author)!=0):
            db=self.Connect()
            cursor=db.cursor()



            sql2 = "SELECT * FROM ((SELECT ISBN, Title, Edition, OnReserve FROM BOOK, AUTHOR WHERE ISBN = AuthorISBN AND Title = (%s) AND AuthorName =(%s)) as table3 NATURAL JOIN (SELECT COUNT(CopyNo), CopyISBN as ISBN FROM BOOKCOPY, AUTHOR WHERE AuthorName = (%s) AND CopyISBN = AuthorISBN AND CheckedOut='No' AND OnHold='No' AND DAMAGED ='No' GROUP BY CopyISBN) as table4)"
            cursor.execute(sql2, (title, author, author))
            self.availBooksList=[]
            self.reserveBooksList=[]
            for i in cursor:
                if i[3] == "No":
                    self.availBooksList.append(i)
                elif i[3] == "Yes":
                    self.reserveBooksList.append(i)
            db.commit()
            self.holdRequest()
        elif (len(title)!=0):
            db=self.Connect()
            cursor=db.cursor()
            sql3 = "SELECT * FROM ((SELECT ISBN, Title, Edition, OnReserve FROM BOOK WHERE Title LIKE %s ) as table3 NATURAL JOIN (SELECT COUNT(CopyNo), CopyISBN as ISBN FROM BOOKCOPY WHERE CheckedOut='No' AND OnHold='No' AND DAMAGED ='No' GROUP BY CopyISBN) as table4)"
            cursor.execute(sql3, (liketitle))
            self.availBooksList=[]
            self.reserveBooksList=[]
            for i in cursor:
                if i[3] == "No":
                    self.availBooksList.append(i)
                elif i[3] == "Yes":
                    self.reserveBooksList.append(i)
            db.commit()
            self.holdRequest()
        elif (len(author)!=0):
            db=self.Connect()
            cursor=db.cursor()
            sql4 = "SELECT * FROM ((SELECT ISBN, Title, Edition, OnReserve FROM BOOK, AUTHOR WHERE ISBN = AuthorISBN AND AuthorName =(%s)) as table3 NATURAL JOIN (SELECT COUNT(CopyNo), CopyISBN as ISBN FROM BOOKCOPY,AUTHOR WHERE CopyISBN = AuthorISBN AND AuthorName =(%s) AND CopyISBN = AuthorISBN AND CheckedOut='No' AND OnHold='No' AND DAMAGED ='No' GROUP BY CopyISBN) as table4)"
            cursor.execute(sql4, (author, author))
            self.availBooksList=[]
            self.reserveBooksList=[]
            for i in cursor:
                if i[3] == "No":
                    self.availBooksList.append(i)
                elif i[3] == "Yes":
                    self.reserveBooksList.append(i)
            db.commit()
            self.holdRequest()
        db.close()




    def holdRequest(self):
        self.HoldRequest=Toplevel(self.win)
        win = self.HoldRequest
        win.title("Hold Request for a Book")



        Label(win, text = "Books Available for Summary").pack()


        BooksFrame = Frame(win, background="black")
        BooksFrame.pack()

        Label(BooksFrame, text = "Select").grid(row=0, column=0, sticky=NSEW, padx=1, pady=1)
        Label(BooksFrame, text = "ISBN").grid(row=0, column=1, sticky=NSEW, padx=1, pady=1)
        Label(BooksFrame, text = "Title of the Book").grid(row=0, column=2, sticky=NSEW, padx=1, pady=1)
        Label(BooksFrame, text = "Edition").grid(row=0, column=3, sticky=NSEW, padx=1, pady=1)
        Label(BooksFrame, text = "# of Copies Available").grid(row=0, column=4, sticky=NSEW, padx=1, pady=1)

        theRow=1
        self.selectedBook=StringVar()
        for item in self.availBooksList:
            Radiobutton(BooksFrame, variable=self.selectedBook, value=item[0]).grid(row=theRow, column=0, sticky=NSEW)
            Label(BooksFrame, text=item[0]).grid(row=theRow,column=1, sticky=NSEW, padx=1, pady=1)
            Label(BooksFrame, text=item[1]).grid(row=theRow,column=2, sticky=NSEW, padx=1, pady=1)
            Label(BooksFrame, text=item[2]).grid(row=theRow,column=3, sticky=NSEW, padx=1, pady=1)
            Label(BooksFrame, text=item[4]).grid(row=theRow,column=4, sticky=NSEW, padx=1, pady=1)
            theRow=theRow+1

        self.holdRequestDate=StringVar()
        self.estReturnDate=StringVar()


        dateFrame = Frame(win)
        dateFrame.pack()
        Label(dateFrame, text = "Hold Request Date: ").grid(row = 0, column = 0)
        holdRequestDateE = Entry(dateFrame, textvariable= self.holdRequestDate, state = DISABLED, disabledforeground="black", disabledbackground="light gray")
        holdRequestDateE.grid(row = 0, column = 1)

        Label(dateFrame, text = "Estimated Return Date: ").grid(row = 0, column = 2)
        estReturnDateE = Entry(dateFrame, textvariable=self.estReturnDate, state = DISABLED, disabledforeground="black", disabledbackground="light gray")
        estReturnDateE.grid(row = 0, column = 3)




        buttonFrame = Frame(win)
        buttonFrame.pack()

        Button(buttonFrame, text = "Back", command = self.searchBack2).grid(row = 0, column = 0, sticky = E)
        Button(buttonFrame, text = "Submit", command = self.submitHoldRequest).grid(row = 0, column = 1, sticky = E) #, command =
        Button(buttonFrame, text = "Close", command = self.destroywin).grid(row = 0, column = 2, sticky = E)



        if (len(self.reserveBooksList)!=0):

            Label(win, text = "Books on Reserve").pack()

            ReserveFrame = Frame(win, background = "black")
            ReserveFrame.pack()

            Label(ReserveFrame, text = "ISBN").grid(row=0, column=0, sticky=NSEW, padx=1, pady=1)
            Label(ReserveFrame, text = "Title of the Book").grid(row=0, column=1, sticky=NSEW, padx=1, pady=1)
            Label(ReserveFrame, text = "Edition").grid(row=0, column=2, sticky=NSEW, padx=1, pady=1)
            Label(ReserveFrame, text = "# of Copies Available").grid(row=0, column=3, sticky=NSEW, padx=1, pady=1)


            resRow=1
            for item in self.reserveBooksList:
                Label(ReserveFrame, text=item[0]).grid(row=theRow,column=0, sticky=NSEW, padx=1, pady=1)
                Label(ReserveFrame, text=item[1]).grid(row=theRow,column=1, sticky=NSEW, padx=1, pady=1)
                Label(ReserveFrame, text=item[2]).grid(row=theRow,column=2, sticky=NSEW, padx=1, pady=1)
                Label(ReserveFrame, text=item[4]).grid(row=theRow,column=3, sticky=NSEW, padx=1, pady=1)
                theRow=theRow+1

    def searchBack(self):
        self.homepage()

    def searchBack2(self):
        self.searchBooks()


    def submitHoldRequest(self):
        currDate=datetime.date.today()
        futureDate=currDate+datetime.timedelta(days=17)

        currDate=str(currDate)
        futureDate=str(futureDate)

        self.holdRequestDate.set(currDate)
        self.estReturnDate.set(futureDate)

        x = self.selectedBook.get()

        db=self.Connect()
        cursor=db.cursor()

        sql = "SELECT CopyISBN, MIN(CopyNo) FROM BOOKCOPY WHERE CopyISBN = %s AND OnHold = 'No' AND CheckedOut = 'No' AND Damaged = 'No'"
        cursor.execute(sql,x)
        result = cursor.fetchall()

        for i in result:
            sql2 = "UPDATE BOOKCOPY SET OnHold='Yes' WHERE CopyISBN = %s AND CopyNo = %s"
            cursor.execute(sql2, (i[0],i[1]))
            ISBN = i[0]
            CopyNo=i[1]

        db.commit()

        y = self.username.get()
        currentDate=datetime.datetime.now().date()
        newDate = currentDate+datetime.timedelta(days=17)

        sql3 = "SELECT MAX(IssueId) FROM ISSUES"
        cursor.execute(sql3)
        result2 = cursor.fetchall()

        for i in result2:
            sql4 = "INSERT INTO ISSUES (IssueUsername, IssueId, DateOfIssue, ReturnDate, IssueCopyNo, IssueISBN) VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql4, (y,i[0]+1,currentDate,newDate,CopyNo,ISBN))
            newId= str(i[0]+1)
            tkMessageBox.showinfo("Submitted!", "You have put a book on hold. Your issue id is %s! "%(newId))

        db.commit()






    def requestExtension(self):

        self.RequestExtension = Toplevel(self.win)
        win = self.RequestExtension
        win.title("Request Extension on a Book")

        Label(win, text = "Enter your Issue_Id").grid(row=0, column=0, sticky=W)
        self.issueId = StringVar()
        issueIdE=Entry(win, textvariable = self.issueId, width=30)
        issueIdE.grid(row=0, column=1, sticky=W)

        submitDatesB=Button(win, text = "Submit", command = self.submitGetDates)
        submitDatesB.grid(row=0, column=2, sticky=W)


        dateFrame = Frame(win, borderwidth=1, relief=SOLID)
        dateFrame.grid(row=1, column=0, columnspan=3)

        Label(dateFrame, text="Original Checkout Date").grid(row=0, column=0)

        self.checkoutDate = StringVar()
        checkoutDateE= Entry(dateFrame, textvariable=self.checkoutDate, disabledforeground="black", disabledbackground="light gray", state=DISABLED)
        checkoutDateE.grid(row=0, column=1)

        Label(dateFrame, text="Current Extension Date").grid(row=1, column=0)

        self.currExtDate = StringVar()
        currExtDateE= Entry(dateFrame, textvariable=self.currExtDate, disabledforeground="black", disabledbackground="light gray", state=DISABLED)
        currExtDateE.grid(row=1, column=1)

        Label(dateFrame, text="Current Return Date").grid(row=1, column=2)

        self.currReturnDate = StringVar()
        currReturnDateE= Entry(dateFrame, textvariable=self.currReturnDate, disabledforeground="black", disabledbackground="light gray", state=DISABLED)
        currReturnDateE.grid(row=1, column=3)

        Label(dateFrame, text="New Extension Date").grid(row=2, column=0)

        self.newExtDate = StringVar()
        newExtDateE= Entry(dateFrame, textvariable=self.newExtDate, disabledforeground="black", disabledbackground="light gray", state=DISABLED)
        newExtDateE.grid(row=2, column=1)

        Label(dateFrame, text="New Estimated Return Date").grid(row=2, column=2)

        self.newReturnDate = StringVar()
        newReturnDateE= Entry(dateFrame, textvariable=self.newReturnDate, disabledforeground="black", disabledbackground="light gray", state=DISABLED)
        newReturnDateE.grid(row=2, column=3)

        submitB=Button(dateFrame, text="Submit", command = self.submitRequestExt)
        submitB.grid(row=3, column=2, columnspan=3, sticky=E)

    def submitGetDates(self):
        self.inte=0

        username=self.username.get()
        issueId=self.issueId.get()
        db=self.Connect()
        cursor=db.cursor()
        futureRequester="No"
        checkedOut="No"
        faculty=""
        currentDate=datetime.datetime.now().date()
        x=0

        sql="SELECT FutureRequester, CheckedOut, IssueUsername FROM BOOKCOPY, ISSUES WHERE IssueISBN=CopyISBN AND IssueId=(%s) AND IssueUsername = (%s)"
        cursor.execute(sql, (issueId, username))



        for i in cursor:
            x=1
            if (str(i[2]) == "None"):
                x=0
            if str(i[0]) == "None":
                y=0
            if (str(i[0]) != "None"):
                futureRequester="Yes"

            if (str(i[1]) == "Yes"):
                checkedOut="Yes"

        if x==0:
            tkMessageBox.showerror("Error", "Cannot find an issue id with your username")
            return None

        if futureRequester=="Yes":
            tkMessageBox.showerror("Sorry!", "There is a future requester on this book so you may not request an extension on this book")
            return None
        if checkedOut=="No":
            tkMessageBox.showerror("Sorry!", "You must check out this book before requesting an extension on it")
            return None

        if (futureRequester=="No" and checkedOut=="Yes"):
            sql2="Select Faculty FROM STUDENTFACULTY, ISSUES WHERE IssueUsername=StudentUsername AND IssueId = (%s)"
            cursor.execute(sql2, issueId)
            for i in cursor:
                faculty=i[0]

            sql3="SELECT CountOfExtension, DateOfIssue, ExtensionDate, ReturnDate FROM ISSUES WHERE IssueId= (%s)"
            cursor.execute(sql3, issueId)
            for i in cursor:
                self.countOfExtension=i[0]
                dateOfIssue=i[1]
                extensionDate=i[2]
                if (str(extensionDate) == "None"):
                    extensionDate=dateOfIssue

                returnDate=i[3]


            if faculty == "No":
                if self.countOfExtension >=2:
                    tkMessageBox.showerror("Sorry!", "You have exceeded the maximum number of extensions for this book")
                    return None
                self.checkoutDate.set(dateOfIssue)
                self.currExtDate.set(extensionDate)
                self.currReturnDate.set(returnDate)
                self.newExtDate.set(currentDate)

                fourteen=currentDate+datetime.timedelta(days=14)
                twentyeight=dateOfIssue+datetime.timedelta(days=28)
                if fourteen > twentyeight:
                    self.newReturnDate.set(twentyeight)
                    self.inte=1
                else:
                    self.newReturnDate.set(fourteen)
                    self.inte=1




            elif faculty == "Yes":
                if self.countOfExtension >=5:
                    tkMessageBox.showerror("Sorry!", "You have exceeded the maximum number of extensions for this book")
                    return None

                self.checkoutDate.set(dateOfIssue)
                self.currExtDate.set(extensionDate)
                self.currReturnDate.set(returnDate)
                self.newExtDate.set(currentDate)

                fourteen=currentDate+datetime.timedelta(14)
                fiftysix=dateOfIssue+datetime.timedelta(56)
                if fourteen > fiftysix:
                    self.newReturnDate.set(fiftysix)
                    self.inte=1
                else:
                    self.newReturnDate.set(fourteen)
                    self.inte=1

        db.commit()
        db.close()



    def submitRequestExt(self):
        if self.inte != 1:
            tkMessageBox.showerror("Error", "You cannot submit an extension")
            return None

        issueId=self.issueId.get()

        db=self.Connect()
        cursor=db.cursor()
        currentDate=datetime.datetime.now().date()
        returnDate=self.newReturnDate.get()
        ext=self.countOfExtension
        ext=ext+1

        sql="UPDATE ISSUES SET ExtensionDate = (%s), ReturnDate = (%s), CountOfExtension=(%s) WHERE IssueId = (%s)"
        cursor.execute(sql, (currentDate, returnDate, ext, issueId))

        db.commit()
        db.close()


    def futureHoldRequest(self):

        self.FutureHoldRequest = Toplevel(self.win)
        win = self.FutureHoldRequest
        win.title("Future Hold Request for a Book")


        Label(win, text="ISBN").grid(row=0, column=0)

        self.holdRequestISBN = StringVar()
        holdRequestISBNE=Entry(win, textvariable=self.holdRequestISBN, width=30)
        holdRequestISBNE.grid(row=0, column=1)

        requestB=Button(win, text="Request", command= self.futureHoldRequestISBN)
        requestB.grid(row=0, column=2)

        otherFrame = Frame(win, borderwidth=1, relief=SOLID)
        otherFrame.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        Label(otherFrame, text="Copy Number:").grid(row=0, column=0)

        self.copyNumber = StringVar()
        copyNumberE=Entry(otherFrame, textvariable = self.copyNumber, state=DISABLED, disabledforeground="black", disabledbackground="light gray")
        copyNumberE.grid(row=0, column=1)

        Label(otherFrame, text="Expected Available Date: ").grid(row=1, column=0)

        self.expectedAvailDate = StringVar()
        expectedAvailDateE=Entry(otherFrame, textvariable = self.expectedAvailDate, state=DISABLED, disabledforeground="black", disabledbackground="light gray")
        expectedAvailDateE.grid(row=1, column=1)


        okB=Button(otherFrame, text="OK", command=self.futureHoldRequestOk)
        okB.grid(row=2, column=1)

    def futureHoldRequestISBN(self):

        ISBN=self.holdRequestISBN.get()
        username=self.username.get()
        db=self.Connect()
        cursor=db.cursor()
        x=0

        sql = "SELECT MAX( ReturnDate ) , IssueCopyNo, IssueISBN FROM BOOKCOPY, ISSUES WHERE (CheckedOut =  'Yes' OR OnHold =  'Yes') AND Damaged =  'No' AND FutureRequester IS NULL AND CopyISBN = IssueISBN AND CopyNo = IssueCopyNo AND IssueISBN = %s"
        cursor.execute(sql, ISBN)

        for i in cursor:
            x=1
            expAvailDate = i[0]
            copyNo= i[1]
            print(copyNo)
            copyISBN=i[2]
            print(copyISBN)
        if (x==1):
            self.expectedAvailDate.set(expAvailDate)
            self.copyNumber.set(copyNo)
            copyNo=self.copyNumber.get()


        sql1 = "UPDATE BOOKCOPY SET OnHold='Yes', FutureRequester=%s WHERE CopyNo=%s AND CopyISBN = %s"
        cursor.execute(sql1, (username,copyNo,ISBN))

        db.commit()
        db.close()
        if str(self.copyNumber.get())=="None":
            tkMessageBox.showerror("Error!", "You cannot put a future request on this book")




    def futureHoldRequestOk(self):
        self.homepage()


    def trackBookLocation(self):

        self.TrackBookLocation = Toplevel(self.win)
        win = self.TrackBookLocation
        win.title("Track Book Location")

        Label(win, text="ISBN").grid(row=0, column=0)

        self.trackISBN= StringVar()
        trackISBNE=Entry(win, textvariable=self.trackISBN)
        trackISBNE.grid(row=0, column=1)

        LocateB=Button(win, text="Locate", command=self.trackBookLocate)
        LocateB.grid(row=0, column=2)

        locationFrame = Frame(win, borderwidth=1, relief=SOLID)
        locationFrame.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        Label(locationFrame, text="Floor Number").grid(row=0, column=0)

        self.floorNumber=StringVar()
        floorNumberE=Entry(locationFrame, textvariable=self.floorNumber, state=DISABLED, disabledforeground="black", disabledbackground="light gray")
        floorNumberE.grid(row=0, column=1)


        Label(locationFrame, text="Aisle Number").grid(row=1, column=0)

        self.aisleNumber=StringVar()
        aisleNumberE=Entry(locationFrame, textvariable=self.aisleNumber, state=DISABLED, disabledforeground="black", disabledbackground="light gray")
        aisleNumberE.grid(row=1, column=1)


        Label(locationFrame, text="Shelf Number").grid(row=0, column=2)

        self.shelfNumber=StringVar()
        shelfNumberE=Entry(locationFrame, textvariable=self.shelfNumber, state=DISABLED, disabledforeground="black", disabledbackground="light gray")
        shelfNumberE.grid(row=0, column=3)


        Label(locationFrame, text="Subject").grid(row=1, column=2)

        self.subject=StringVar()
        subjectE=Entry(locationFrame, textvariable=self.subject, state=DISABLED, disabledforeground="black",  disabledbackground="light gray")
        subjectE.grid(row=1, column=3)

    def trackBookLocate(self):
        ISBN=self.trackISBN.get()
        db=self.Connect()
        cursor=db.cursor()

        sql = "SELECT BookSubject, BookShelf, AisleNo, ShelfFloorNo FROM BOOK, SHELF, SUBJECT WHERE ISBN = (%s) AND BookShelf=ShelfNo AND SubjectName = BookSubject AND SubjectFloorNo=ShelfFloorNo AND AisleNo=BookAisleNo"
        cursor.execute(sql, (ISBN))

        for i in cursor:
            self.floorNumber.set(i[3])
            self.aisleNumber.set(i[2])
            self.subject.set(i[0])
            self.shelfNumber.set(i[1])



    def bookCheckout(self):
        self.bookCheckout = Toplevel(self.win)
        win = self.bookCheckout
        win.title("Book Checkout")


        Label(win, text="Issue Id").grid(row=0, column=0)
        self.issueIdcheckout=StringVar()
        issueIdcheckoutE=Entry(win, textvariable=self.issueIdcheckout)
        issueIdcheckoutE.grid(row=0, column=1)


        Label(win, text="User Name").grid(row=0, column=2)
        self.usernamecheckout= StringVar()
        usernamecheckoutE=Entry(win, textvariable=self.usernamecheckout, state=DISABLED, disabledforeground="black", disabledbackground="light gray")
        usernamecheckoutE.grid(row=0, column=3)

        Label(win, text="ISBN").grid(row=1, column=0)
        self.ISBNcheckout=StringVar()
        ISBNcheckoutE=Entry(win, textvariable=self.ISBNcheckout, state=DISABLED, disabledforeground="black", disabledbackground="light gray")
        ISBNcheckoutE.grid(row=1, column=1)

        Label(win, text="Copy #").grid(row=1, column=2)
        self.copyNocheckout=StringVar()
        copyNocheckoutE=Entry(win, textvariable=self.copyNocheckout, state=DISABLED, disabledforeground="black", disabledbackground="light gray")
        copyNocheckoutE.grid(row=1, column=3)

        Label(win, text="Checkout Date").grid(row=2, column=0)
        self.checkoutDate=StringVar()
        checkoutDateE=Entry(win, textvariable=self.checkoutDate, state=DISABLED, disabledforeground="black", disabledbackground="light gray")
        checkoutDateE.grid(row=2, column=1)

        Label(win, text="Estimated Return Date").grid(row=2, column=2)
        self.checkoutReturnDate=StringVar()
        checkoutReturnDateE=Entry(win, textvariable=self.checkoutReturnDate, state=DISABLED, disabledforeground="black", disabledbackground="light gray")
        checkoutReturnDateE.grid(row=2, column=3)


        ConfirmB=Button(win, text="Confirm", command=self.infoCheckout)
        ConfirmB.grid(row=3, column=0, columnspan=4)

    def infoCheckout(self):
        issueId=self.issueIdcheckout.get()


        currDate=datetime.date.today()
        futureDate=currDate+datetime.timedelta(days=14)

        self.checkoutDate.set(currDate)
        self.checkoutReturnDate.set(futureDate)

        db=self.Connect()
        cursor=db.cursor()
        x=0

        sql0="SELECT IssueUsername, IssueCopyNo, IssueISBN, DateOfIssue FROM ISSUES, BOOKCOPY WHERE IssueId = (%s) AND OnHold = 'Yes' AND CheckedOut= 'No' AND IssueISBN=CopyISBN AND CopyNo=IssueCopyNo"
        cursor.execute(sql0, (issueId))
        for i in cursor:
            username = i[0]
            self.usernamecheckout.set(username)
            copyNo=i[1]
            self.copyNocheckout.set(copyNo)
            ISBN=i[2]
            self.ISBNcheckout.set(ISBN)
            DateOfIssue=i[3]
            x=1
            if str(i[0]) == "None":
                x=0

        if (self.usernamecheckout.get() == ""):

            tkMessageBox.showerror("Error", "No on hold book for that issue id!")
            return None




        if x==1:
            if ((DateOfIssue+datetime.timedelta(days=3)) <= currDate):

                tkMessageBox.showerror("Error!", "You waited longer than three days and will be dropped from the database")
                sql = "UPDATE BOOKCOPY SET OnHold='No' WHERE CopyISBN = (%s) AND CopyNo= (%s)"
                cursor.execute(sql, (ISBN, copyNo))
                db.commit()
                db.close()
                db=self.Connect()
                cursor=db.cursor()
                sql="DELETE * FROM ISSUES WHERE IssueId = (%s)"
                cursor.execute(sql, issueId)

                self.homepage()
                x=0
                return None


            else:
                currDate=str(currDate)
                futureDate=str(futureDate)
                sql="UPDATE BOOKCOPY SET OnHold='No', CheckedOut='Yes' WHERE CopyISBN=(%s) AND CopyNo=(%s)"
                cursor.execute(sql, (ISBN, copyNo))
                db.commit()
                db.close()
                db2=self.Connect()
                cursor2=db2.cursor()

                sql2="UPDATE ISSUES SET DateOfIssue = (%s), ReturnDate = (%s) WHERE IssueId = (%s)"
                cursor2.execute(sql2, (currDate, futureDate, issueId))

                db2.commit()
                db2.close()














    def returnBook(self):

        self.ReturnBook = Toplevel(self.win)
        win = self.ReturnBook
        win.title("Return Book")

        Label(win, text="Issue Id").grid(row=0, column=0)
        self.returnIssueId = StringVar()
        returnIssueIdE=Entry(win, textvariable=self.returnIssueId)
        returnIssueIdE.grid(row=0, column=1)

        Label(win, text="ISBN").grid(row=1, column=0)
        self.returnISBN=StringVar()
        returnISBNE=Entry(win, textvariable=self.returnISBN, state=DISABLED, disabledforeground="black", disabledbackground="light gray")
        returnISBNE.grid(row=1, column=1)

        Label(win, text="Copy Number").grid(row=1, column=2)
        self.returnCopyNo=StringVar()
        returnCopyNoE=Entry(win, textvariable=self.returnCopyNo, state=DISABLED, disabledforeground="black", disabledbackground="light gray")
        returnCopyNoE.grid(row=1, column=3)

        Label(win, text="Return in Damaged Condition").grid(row=2, column=0)
        self.returnDamaged=StringVar()
        returnDamagedE = OptionMenu(win, self.returnDamaged, "N", "Y")
        returnDamagedE.grid(row=2, column=1)

        Label(win, text="User Name").grid(row=2, column=2)
        self.returnUsername=StringVar()
        returnUsernameE=Entry(win, textvariable=self.returnUsername, state=DISABLED, disabledforeground="black", disabledbackground="light gray")
        returnUsernameE.grid(row=2, column=3)


        actualreturnB=Button(win, text="Return", command=self.returnBookB)
        actualreturnB.grid(row=3, column=2, columnspan=1, stick=EW)



    def returnBookB(self):
        if (self.returnIssueId.get()=="" or self.returnDamaged.get()==""):
            tkMessageBox.showerror("Error!", "Please fill out the issue id and if the book is damaged.")
            return None
        issueId=self.returnIssueId.get()
        damaged=self.returnDamaged.get()
        currDate=datetime.date.today()
        db=self.Connect()
        cursor=db.cursor()
        x=0


        sql0 = "SELECT IssueUsername FROM ISSUES, BOOKCOPY WHERE IssueId=(%s) AND CopyISBN = IssueISBN AND CopyNo = IssueCopyNo AND CheckedOut='Yes'"
        cursor.execute(sql0, (issueId))

        for i in cursor:
            x=1
            if str(i[0]) == "None":
                x=0
            username = i[0]
            self.returnUsername.set(i[0])

        sql = "SELECT IssueISBN, IssueCopyNo, ReturnDate FROM ISSUES, BOOKCOPY WHERE IssueId=(%s) AND CopyISBN = IssueISBN AND CopyNo = IssueCopyNo AND CheckedOut='Yes'"

        cursor.execute(sql, (issueId))
        for i in cursor:
            expectedReturnDate=i[2]
            self.returnISBN.set(i[0])
            self.returnCopyNo.set(i[1])
        db.commit()
        db.close()


        ISBN=self.returnISBN.get()
        copyNo=self.returnCopyNo.get()


        db=self.Connect()
        cursor=db.cursor()

        if x==0:
            tkMessageBox.showerror("Error!", "Cannot find a checked out book with that issue id")
            return None



        if (self.returnDamaged.get() == "Y"):

            sql = "UPDATE BOOKCOPY SET CheckedOut='No', Damaged='Yes' WHERE CopyISBN= (%s) AND CopyNo=(%s)"
            cursor.execute(sql, (ISBN, copyNo))
            db.commit()
            db.close()
            db2=self.Connect()
            cursor2=db2.cursor()

            sql2 = "UPDATE ISSUES SET ActualReturnDate = (%s) WHERE IssueISBN = (%s) AND IssueCopyNo = (%s)"
            cursor.execute(sql2, (currDate, ISBN, copyNo))
            db.close()
            db.commit()





        if (self.returnDamaged.get() == "N"):

            sql = "UPDATE BOOKCOPY SET CheckedOut='No' WHERE (CopyISBN= (%s) AND CopyNo=(%s))"
            cursor.execute(sql, (ISBN, copyNo))

            db.commit()
            db.close()

            db1=self.Connect()
            cursor1=db1.cursor()
            sql1 = "UPDATE BOOKCOPY SET Damaged='No' WHERE (CopyISBN= (%s) AND CopyNo=(%s))"
            cursor1.execute(sql1, (ISBN, copyNo))

            db1.commit()
            db1.close()

            db2=self.Connect()
            cursor2=db2.cursor()


            sql2 = "UPDATE ISSUES SET ActualReturnDate = (%s) WHERE IssueISBN = (%s) AND IssueCopyNo = (%s)"
            cursor2.execute(sql2, (currDate, ISBN, copyNo))

            db2.commit()
            db2.close()

        if expectedReturnDate < currDate:
            delta = currDate-expectedReturnDate
            daystoPay=delta.days
            fine = float(.5*daystoPay)
            db=self.Connect()
            cursor=db.cursor()
            username = self.returnUsername.get()
            sql = "SELECT PENALTY FROM STUDENTFACULTY WHERE StudentUsername = (%s)"
            cursor.execute(sql, username)
            for i in cursor:
                fine = fine + float(i[0])

            sql = "UPDATE STUDENTFACULTY SET PENALTY = (%s) WHERE StudentUsername = (%s)"
            cursor.execute(sql, (fine, username))
            db.commit()
            db.close()






    def lostDamagedBook(self):

        self.LostDamagedBook = Toplevel(self.win)
        win = self.LostDamagedBook
        win.title("Lost/Damaged Book")



        Label(win, text="ISBN").grid(row=0, column=0)
        self.lostISBN=StringVar()
        lostISBNE=Entry(win, textvariable=self.lostISBN)
        lostISBNE.grid(row=0, column=1)

        Label(win, text="Book Copy #").grid(row=0, column=2)
        self.lostCopyNo=StringVar()
        lostCopyNoE=Entry(win, textvariable=self.lostCopyNo)
        lostCopyNoE.grid(row=0, column=3)

        Label(win, text="Current Time").grid(row=1, column=0)
        self.lostTime=StringVar()
        self.lostTime.set(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M')))
        lostTimeE=Entry(win, textvariable=self.lostTime, state=DISABLED, disabledforeground="black", disabledbackground="light gray")

        lostTimeE.grid(row=1, column=1)

        lookB=Button(win, text="Look for the last user", command=self.lastUser)
        lookB.grid(row=2, column=0, columnspan=4)

        userFrame = Frame(win, borderwidth=1, relief=SOLID)
        userFrame.grid(row=3, column=0, columnspan=4, sticky=NSEW)

        Label(userFrame, text="Last User of the Book").grid(row=0, column=0)
        self.lostUser= StringVar()
        lostUserE=Entry(userFrame, textvariable=self.lostUser, state=DISABLED, disabledforeground="black", disabledbackground="light gray")
        lostUserE.grid(row=0, column=1)

        Label(userFrame, text="Amount to be charged").grid(row=1, column=0)
        self.lostCharge= StringVar()
        lostChargeE=Entry(userFrame, textvariable=self.lostCharge)
        lostChargeE.grid(row=1, column=1)

        self.submitB=Button(userFrame, text="Submit", command=self.submitLost)
        self.submitB.grid(row=2, column=1,sticky=E)

        cancelB=Button(userFrame, text="Cancel", command=self.cancel)
        cancelB.grid(row=2, column=2, sticky=W)

    def lastUser(self):
        ISBN=self.lostISBN.get()
        copyNo=self.lostCopyNo.get()
        currTime=self.lostTime.get()
        x=0

        db=self.Connect()
        cursor=db.cursor()

        sql="SELECT MAX(ReturnDate) FROM ISSUES WHERE IssueISBN = (%s) AND IssueCopyNo = (%s)"
        cursor.execute(sql, (ISBN, copyNo))

        for i in cursor:
            x=1
            if str(i[0]) == "None":
                x=0
            returnDate = i[0]

        sql="SELECT IssueUsername FROM ISSUES WHERE IssueISBN = (%s) AND IssueCopyNo = (%s) AND ReturnDate = (%s)"
        cursor.execute(sql, (ISBN, copyNo, returnDate))
        for i in cursor:
            x=1
            if str(i[0]) == "None":
                x=0
            user = i[0]
            self.lostUser.set(user)
            db.commit()
            db.close()
        if x==0:
            tkMessageBox.showerror("Error", "Cannot find user with that isbn and copy number.")
            self.submitB.state(["disabled"])
            return None
    def submitLost(self):
        charge=int(self.lostCharge.get())
        user=self.lostUser.get()
        ISBN=self.lostISBN.get()
        copyNo=self.lostCopyNo.get()

        db=self.Connect()
        cursor=db.cursor()

        sql = "SELECT PENALTY FROM STUDENTFACULTY WHERE StudentUsername = (%s)"
        cursor.execute(sql, user)
        result =cursor.fetchall()
        for i in result:
            penalty= int(i[0])
            print(penalty)

        sql2="UPDATE STUDENTFACULTY SET Penalty = (%s) WHERE StudentUsername = (%s)"
        cursor.execute(sql2, (str(charge+penalty), user))
        db.commit()

        cursor=db.cursor()

        sql3="UPDATE BOOKCOPY SET Damaged='Yes' WHERE CopyISBN = (%s) AND CopyNo = (%s)"
        cursor.execute(sql3, (ISBN, copyNo))

        tkMessageBox.showinfo("Submitted!", "You have charged the user.")
        db.commit()
        db.close()

    def cancel(self):
        win.withdraw()
        self.homepage()






###reports

    def damagedBooksReport(self):

        self.DamagedBooksReport = Toplevel(self.win)
        win = self.DamagedBooksReport
        win.title("Damaged Books Report")

        Label(win, text="Month").grid(row=0, column=0)
        self.monthDBR=StringVar()
        monthDBRE=OptionMenu(win,self.monthDBR,"January", "February", "March")
        monthDBRE.grid(row=0, column=1)


        Label(win, text="Subject").grid(row=0, column=2)

        self.subject1DBR=StringVar()
        subject1DBRE=OptionMenu(win, self.subject1DBR, "Science", "Math", "History", "Poetry")
        subject1DBRE.grid(row=0, column=3)

        Label(win, text="Subject").grid(row=1, column=2)

        self.subject2DBR=StringVar()
        subject2DBRE=OptionMenu(win, self.subject2DBR, "Science", "Math", "History", "Poetry")
        subject2DBRE.grid(row=1, column=3)

        Label(win, text="Subject").grid(row=2, column=2)

        self.subject3DBR=StringVar()
        subject3DBRE=OptionMenu(win, self.subject3DBR, "Science", "Math", "History", "Poetry")
        subject3DBRE.grid(row=2, column=3)

        showReportB=Button(win, text="Show Report", command=self.damagedReport) ##command= show report
        showReportB.grid(row=3, column=0, columnspan=4)

    def damagedReport(self):

        win = self.DamagedBooksReport

        reportFrame = Frame(win, background="black")
        reportFrame.grid(row=4, column=0, columnspan=4)

        Label(reportFrame, text="Month", width=16).grid(row=0, column=0, padx=1, pady=1)
        Label(reportFrame, text="Subject", width=16).grid(row=0, column=1, padx=1, pady=1)

        month=str(self.monthDBR.get())
        monthE=Entry(reportFrame, text=month, width=15, state=DISABLED, disabledforeground="black")
        monthE.grid(row=2, column=0, padx=1, pady=1)


        Entry(reportFrame, text="", width=15, state=DISABLED).grid(row=1, column=0, padx=1, pady=1)
        Entry(reportFrame, text="", width=15, state=DISABLED).grid(row=3, column=0, padx=1, pady=1)

        subject1=str(self.subject1DBR.get())
        subject1E=Entry(reportFrame, text=subject1, width=15, state=DISABLED, disabledforeground="black")
        subject1E.grid(row=1, column=1, padx=1, pady=1)

        subject2=str(self.subject2DBR.get())
        subject2E=Entry(reportFrame, text=subject2, width=15, state=DISABLED, disabledforeground="black")
        subject2E.grid(row=2, column=1, padx=1, pady=1)

        subject3=str(self.subject3DBR.get())
        subject3E=Entry(reportFrame, text=subject3, width=15, state=DISABLED, disabledforeground="black")
        subject3E.grid(row=3, column=1, padx=1, pady=1)


        Label(reportFrame, text="#damaged books",width=21).grid(row=0, column=2, padx=1, pady=1)
#####################################################
        db=self.Connect()
        cursor=db.cursor()

        if month == "January":
            monthnum = 1
        elif month == "February":
            monthnum = 2
        elif month == "March":
            monthnum = 3

        sql1 = "SELECT IssueCopyNo, IssueISBN, MAX(MONTH(ReturnDate)) FROM BOOK, ISSUES, BOOKCOPY WHERE BookSubject = %s AND CopyISBN = ISBN AND IssueISBN = CopyISBN AND Damaged = 'Yes' AND IssueCopyNo = CopyNo GROUP BY IssueISBN, IssueCopyNo"
        cursor.execute(sql1, (subject1))
        result = cursor.fetchall()
        count1 = 0
        for i in result:
            if i[2] == monthnum:
                count1 = count1 + 1

        sql2 = "SELECT IssueCopyNo, IssueISBN, MAX(MONTH(ReturnDate)) FROM BOOK, ISSUES, BOOKCOPY WHERE BookSubject = %s AND CopyISBN = ISBN AND IssueISBN = CopyISBN AND Damaged = 'Yes' AND IssueCopyNo = CopyNo GROUP BY IssueISBN, IssueCopyNo"
        cursor.execute(sql2, (subject2))
        result = cursor.fetchall()
        count2 = 0
        for i in result:
            if i[2] == monthnum:
                count2 = count2 + 1

        sql3 = "SELECT IssueCopyNo, IssueISBN, MAX(MONTH(ReturnDate)) FROM BOOK, ISSUES, BOOKCOPY WHERE BookSubject = %s AND CopyISBN = ISBN AND IssueISBN = CopyISBN AND Damaged = 'Yes' AND IssueCopyNo = CopyNo GROUP BY IssueISBN, IssueCopyNo"
        cursor.execute(sql3, (subject3))
        result = cursor.fetchall()
        count3 = 0
        for i in result:
            if i[2] == monthnum:
                count3 = count3 + 1



        num1=str(count1)
        num2=str(count2)
        num3=str(count3)

        num1E=Label(reportFrame, text=num1, width=18, height=1, state=DISABLED, disabledforeground="black")
        num1E.grid(row=1, column=2, padx=1, pady=1)


        num2E=Label(reportFrame, text=num2, width=18, height=1, state=DISABLED, disabledforeground="black")
        num2E.grid(row=2, column=2,padx=1, pady=1)

        num3E=Label(reportFrame, text=num3, width=18,height=1, state=DISABLED, disabledforeground="black")
        num3E.grid(row=3, column=2, padx=1, pady=1)

    def popularBooksReport(self):

        self.PopularBooksReport = Toplevel(self.win)
        win = self.PopularBooksReport
        win.title("Popular Books Report")

        reportFrame = Frame(win, background="black")
        reportFrame.grid(row=0, column=0)

        Label(reportFrame, text="Month", width=15).grid(row=0, column=0, padx=1, pady=1)
        Label(reportFrame, text="Title", width=15).grid(row=0, column=1, padx=1, pady=1)
        Label(reportFrame, text="#checkouts", width=15).grid(row=0, column=2, padx=1, pady=1)


        monthE=Label(reportFrame, text="January", width=15)
        monthE.grid(row=1, column=0, padx=1, pady=1)


        Label(reportFrame, text="", width=15).grid(row=2, column=0)
        Label(reportFrame, text="", width=15).grid(row=3, column=0)

        Label(reportFrame, text="February", width=15).grid(row=4, column=0, padx=1, pady=1)

        Label(reportFrame, text="", width=15).grid(row=5, column=0)
        Label(reportFrame, text="", width=15).grid(row=6, column=0)

        db=self.Connect()
        cursor=db.cursor()

        sql1 = "SELECT COUNT(DateOfIssue), Title FROM ISSUES, BOOK WHERE MONTH(DateOfIssue)='1' AND ISBN = IssueISBN GROUP BY IssueISBN ORDER BY COUNT(DateOfIssue) DESC"
        cursor.execute(sql1)
        result=cursor.fetchall()

        for i in range(0,3):
            Label(reportFrame,text=str(result[i][1]),width=15).grid(row=i+1,column=1)
            Label(reportFrame,text=str(result[i][0]),width=15).grid(row=i+1,column=2)


        sql2 = "SELECT COUNT(DateOfIssue), Title FROM ISSUES, BOOK WHERE MONTH(DateOfIssue)='2' AND ISBN = IssueISBN GROUP BY IssueISBN ORDER BY COUNT(DateOfIssue) DESC"
        cursor.execute(sql2)
        result=cursor.fetchall()

        for i in range(0,3):
            Label(reportFrame,text=str(result[i][1]),width=15).grid(row=i+4,column=1)
            Label(reportFrame,text=str(result[i][0]),width=15).grid(row=i+4,column=2)




        db.commit()
        db.close()

    def frequentUserReport(self):
        self.FrequentUserReport = Toplevel(self.win)
        win = self.FrequentUserReport
        win.title("Frequent Users Report")

        reportFrame = Frame(win, background="black")
        reportFrame.grid(row=0, column=0)

        Label(reportFrame, text="Month", width=15).grid(row=0, column=0, padx=1, pady=1)
        Label(reportFrame, text="Username", width=15).grid(row=0, column=1, padx=1, pady=1)
        Label(reportFrame, text="#checkouts", width=15).grid(row=0, column=2, padx=1, pady=1)


        monthE=Label(reportFrame, text="January", width=15)
        monthE.grid(row=1, column=0, padx=1, pady=1)

        db=self.Connect()
        cursor=db.cursor()

        sql1= "SELECT COUNT( IssueUsername ) , IssueUsername FROM ISSUES WHERE MONTH( DateOfIssue ) =  '1' GROUP BY IssueUsername ORDER BY (COUNT( IssueUsername )) DESC"
        cursor.execute(sql1)
        result=cursor.fetchall()
        print result


        end = len(result)
        for i in range(0,end):
            if result[i][0]>10:
                if i>5:
                    pass
                else:
                    Label(reportFrame, text=str(result[i][1]), width=15).grid(row=i+1,column=1)
                    Label(reportFrame, text=str(result[i][0]), width =15).grid(row=i+1,column=2)
                    if i>0:
                        Label(reportFrame,text="",width=15).grid(row=i+1,column=0)

        sql2 = "SELECT COUNT( IssueUsername ) , IssueUsername FROM ISSUES WHERE MONTH( DateOfIssue ) =  '2' GROUP BY IssueUsername ORDER BY COUNT(IssueUsername) DESC"
        cursor.execute(sql2)
        result2 = cursor.fetchall()


        Label(reportFrame, text="February", width=15).grid(row=end+1,column=0)
        end2= len(result2)

        for s in range(0,end2):
            if result2[s][0]>10:
                if s>5:
                    pass
                else:
                    Label(reportFrame, text=str(result2[s][1]), width=15).grid(row=end+1+s, column=1)
                    Label(reportFrame, text=str(result2[s][0]), width=15).grid(row=end+1+s, column=2)
                    if s>0:
                        Label(reportFrame, text="", width=15).grid(row=end+1+s, column=0)

        db.commit()
        db.close()


    def popularSubjectReport(self):
        self.PopularSubjectReport = Toplevel(self.win)
        win = self.PopularSubjectReport
        win.title("Popular Subject Report")

        reportFrame = Frame(win, background="black")
        reportFrame.grid(row=0, column=0)

        Label(reportFrame, text="Month", width=15).grid(row=0, column=0, padx=1, pady=1)
        Label(reportFrame, text="Top Subject", width=15).grid(row=0, column=1, padx=1, pady=1)
        Label(reportFrame, text="#checkouts", width=15).grid(row=0, column=2, padx=1, pady=1)


        monthE=Label(reportFrame, text="January", width=15)
        monthE.grid(row=1, column=0, padx=1, pady=1)

        Label(reportFrame, text="", width=15).grid(row=2, column=0)
        Label(reportFrame, text="", width=15).grid(row=3, column=0) ##top three

        Label(reportFrame, text="February", width=15).grid(row=4, column=0, padx=1, pady=1)

        Label(reportFrame, text="", width=15).grid(row=5, column=0)
        Label(reportFrame, text="", width=15).grid(row=6, column=0)


        db=self.Connect()
        cursor=db.cursor()

        sql="SELECT COUNT(DateOfIssue), BookSubject FROM ISSUES, BOOK WHERE MONTH(DateOfIssue)='1' AND ISBN = IssueISBN GROUP BY BookSubject ORDER BY COUNT(DateOfIssue) DESC"
        cursor.execute(sql)
        x=-1
        for i in cursor:
            x=x+1
            if x>2:
                pass
            elif x<=2:
                print
                Label(reportFrame, text=str(i[1]), width=15).grid(row=x+1, column=1)
                Label(reportFrame, text=str(i[0]), width=15).grid(row=x+1, column=2)


        db.commit()
        db.close()

        db=self.Connect()
        cursor=db.cursor()

        sql="SELECT COUNT(DateOfIssue), BookSubject FROM ISSUES, BOOK WHERE MONTH(DateOfIssue)='2' AND ISBN = IssueISBN GROUP BY BookSubject ORDER BY COUNT(DateOfIssue) DESC"
        cursor.execute(sql)
        y=0
        for j in cursor:

            if y>2:
                pass
            elif y<=2:
                print
                Label(reportFrame, text=str(j[1]), width=15).grid(row=x+1, column=1)
                Label(reportFrame, text=str(j[0]), width=15).grid(row=x+1, column=2)
            x=x+1
            y=y+1








win=Tk()
app=library(win)
win.mainloop()

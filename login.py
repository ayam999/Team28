def ChooseToCompanion():
    Choose_AccountFrame.destroy()
    LoginCompanionForm()
def ChooseToLogin():
    Choose_AccountFrame.destroy()
    LoginForm()
USERNAME = StringVar()
PASSWORD = StringVar()
ID = StringVar()
EMAIL = StringVar()
FN = StringVar()
LN = StringVar()
Developer= StringVar()
Developerpass= StringVar()
def LoginCompanionForm():
    global LoginCompanionFrame, lbl_resul1

    LoginCompanionFrame = Frame(app)
    LoginCompanionFrame.pack()

    lbl_result_empty = Label(LoginCompanionFrame, text="Login For developer", font=('arial', 18), fg="blue")
    lbl_result_empty.grid(row=0, columnspan=2)

    lbl_username = Label(LoginCompanionFrame, text="developer Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=2)

    lbl_password = Label(LoginCompanionFrame, text="developer Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=3)

    lbl_resul1 = Label(LoginCompanionFrame, text="", font=('arial', 18))
    lbl_resul1.grid(row=4, columnspan=2)

    username = Entry(LoginCompanionFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=2, column=1)


    password = Entry(LoginCompanionFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=3, column=1)


    btn_login = Button(LoginCompanionFrame, text="Login", font=('arial', 18), width=35, command=LoginCompanion,
                       fg='red')
    btn_login.grid(row=5, columnspan=2, pady=20)


    btne_register = Button( LoginCompanionFrame, text="Creat Account", fg="red", width=35, font=('arial', 18),
                           command=ToggleToRegister2)
    btne_register.grid(row=6, columnspan=2, pady=20)
def ToggleToRegister2():
    LoginCompanionFrame.destroy()
    RegisterForm1()
def LoginCompanion():
    Database()

    if Developer.get == "" or Developerpass.get() == "":
        lbl_resul1.config(text="Empty fields!", fg="purple")
    else:
        cursor.execute("SELECT * FROM `developer` WHERE `username` = ? and `password` = ?",
                       (Developer.get(), Developerpass.get()))
        if cursor.fetchone() is not None:
            lbl_resul1.config(text="You Successfully Login", fg="blue")#, command=ToCompanion())
        else:
            lbl_resul1.config(text="Invalid Username or password", fg="red")

user=StringVar()
phn=StringVar()
eml=StringVar()

def LoginForm():
    global LoginFrame, lbl_result1

    LoginFrame = Frame(app)
    LoginFrame.pack()

    lbl_result_empty = Label(LoginFrame, text="Login For admin", font=('arial', 18), fg="blue")
    lbl_result_empty.grid(row=0, columnspan=2)

    lbl_username = Label(LoginFrame, text="admin Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=2)

    lbl_password = Label(LoginFrame, text="admin Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=3)

    lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
    lbl_result1.grid(row=4, columnspan=2)

    username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=2, column=1)
    user=USERNAME

    password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=3, column=1)


    btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=Login, fg='red')
    btn_login.grid(row=5, columnspan=2, pady=20)

    btne_register = Button(LoginFrame, text="Creat Account", fg="red", width=35, font=('arial', 18), command=ToggleToRegister1)
    btne_register.grid(row=6, columnspan=2, pady=20)
def ToggleToRegister1():
    LoginFrame.destroy()
    RegisterForm()
global LoginFrame
def RegisterForm():
    global RegisterFrame11, lbl_result2, last
    last=datetime

    RegisterFrame11 = Frame(app)
    RegisterFrame11.pack()

    lbl_result_empty = Label(RegisterFrame11, text="Register For admin", font=('arial', 18), fg="blue")
    lbl_result_empty.grid(row=0, columnspan=2)

    lbl_username = Label(RegisterFrame11, text="admin Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=2)

    lbl_password = Label(RegisterFrame11, text="admin Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=3)

    lbl_idnum = Label(RegisterFrame11, text="admin id number:", font=('arial', 18), bd=18)
    lbl_idnum.grid(row=4)


    lbl_email = Label(RegisterFrame11, text="admin email:", font=('arial', 18), bd=18)
    lbl_email.grid(row=5)

    lbl_fn = Label(RegisterFrame11, text="admin first name:", font=('arial', 18), bd=18)
    lbl_fn.grid(row=6)

    lbl_ln = Label(RegisterFrame11, text="admin last name:", font=('arial', 18), bd=18)
    lbl_ln.grid(row=7)

    lbl_result2 = Label(RegisterFrame11, text="", font=('arial', 18))
    lbl_result2.grid(row=8, columnspan=2)

    username = Entry(RegisterFrame11, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=2, column=1)

    password = Entry(RegisterFrame11, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=3, column=1)

    idnumber = Entry(RegisterFrame11, font=('arial', 20), textvariable=ID, width=15)
    idnumber.grid(row=4, column=1)

    email = Entry(RegisterFrame11, font=('arial', 20), textvariable=EMAIL, width=15)
    email.grid(row=5, column=1)

    fn = Entry(RegisterFrame11, font=('arial', 20), textvariable=FN, width=15)
    fn.grid(row=6, column=1)

    ln = Entry(RegisterFrame11, font=('arial', 20), textvariable=LN, width=15)
    ln.grid(row=7, column=1)

    btn_login = Button(RegisterFrame11, text="Register", font=('arial', 18), width=35, command=Register, fg='red')
    btn_login.grid(row=8, columnspan=2, pady=20)

    btne_login = Button(RegisterFrame11, text="Return To Login", fg="red", width=35, font=('arial', 18),
                        command=ToggleToLogin)
    btne_login.grid(row=9, columnspan=2, pady=20)
def ToggleToLogin():
    RegisterFrame11.destroy()
    LoginForm()
def Login():
    Database()
#11
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Empty fields!", fg="purple")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? and `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            lbl_result1.config(text="You Successfully Login", fg="blue")#, command=ToCompanion())
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")

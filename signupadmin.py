
def Register():

    Database()
    if USERNAME.get == "" or PASSWORD.get() == "" or ID.get() == "" or EMAIL.get() == "":
        lbl_result2.config(text="Empty fields!", fg="purple")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ?", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Username is already taken", fg="red")
        cursor.execute("SELECT * FROM `developer` WHERE `username` = ?", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Username is already taken", fg="red")

        else:
            insert_admin(str(USERNAME.get()), str(PASSWORD.get()), str(ID.get()), str(EMAIL.get()), str(FN.get()), str(LN.get()))
            insert_Developer(str(USERNAME.get()), str(PASSWORD.get()), str(ID.get()), str(EMAIL.get()), str(FN.get()), str(LN.get()))
            USERNAME.set("")
            PASSWORD.set("")
            ID.set("")
            EMAIL.set("")
            FN.set("")
            LN.set("")
            lbl_result2.config(text="Successfully Created!", fg="black")
        cursor.close()
        conn.close()




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
    #######################################################


def insert_admin(username, password, num, email, f, l):
    try:
        cursor.execute("INSERT INTO `admin` (username, password, id, email,firstname,lastname) VALUES(?, ?, ?, ?, ?, ?)", (username, password, num, email,f,l))
        conn.commit()
    except ValueError:
        print(ValueError)

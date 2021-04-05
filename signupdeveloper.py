
def insert_Developer(username, password, num, email, f, l):
    try:
        cursor.execute("INSERT INTO `developer` (username, password, id, email,firstname,lastname) VALUES(?, ?, ?, ?, ?, ?)", (username, password, num, email,f,l))
        conn.commit()
    except ValueError:
        print(ValueError)


#end log in
def RegisterForm1():
    global RegisterFrame, lbl_result2

    RegisterFrame = Frame(app)
    RegisterFrame.pack()

    lbl_result_empty = Label(RegisterFrame, text="Register For developer", font=('arial', 18), fg="blue")
    lbl_result_empty.grid(row=0, columnspan=2)

    lbl_username = Label(RegisterFrame, text="developer Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=2)

    lbl_password = Label(RegisterFrame, text="developer Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=3)

    lbl_idnum = Label(RegisterFrame, text="developer id number:", font=('arial', 18), bd=18)
    lbl_idnum.grid(row=4)

    lbl_email = Label(RegisterFrame, text="developer email:", font=('arial', 18), bd=18)
    lbl_email.grid(row=5)


    lbl_fn = Label(RegisterFrame, text="admin first name:", font=('arial', 18), bd=18)
    lbl_fn.grid(row=6)

    lbl_ln = Label(RegisterFrame, text="admin last name:", font=('arial', 18), bd=18)
    lbl_ln.grid(row=7)

    lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
    lbl_result2.grid(row=8, columnspan=2)

    username = Entry(RegisterFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=2, column=1)

    password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=3, column=1)

    idnumber = Entry(RegisterFrame, font=('arial', 20), textvariable=ID, width=15)
    idnumber.grid(row=4, column=1)

    email = Entry(RegisterFrame, font=('arial', 20), textvariable=EMAIL, width=15)
    email.grid(row=5, column=1)


    fn = Entry(RegisterFrame, font=('arial', 20), textvariable=FN, width=15)
    fn.grid(row=6, column=1)

    ln = Entry(RegisterFrame, font=('arial', 20), textvariable=LN, width=15)
    ln.grid(row=7, column=1)

    btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=Register, fg='red')
    btn_login.grid(row=8, columnspan=2, pady=20)

    btne_login = Button(RegisterFrame, text="Return To Login", fg="red", width=35, font=('arial', 18),
                        command=tocust)
    btne_login.grid(row=9, columnspan=2, pady=20)

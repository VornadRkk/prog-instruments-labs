import tkinter
import tkinter.messagebox as tm

import mysql.connector




# First Create the Database after run this program#
"""Create Database name as logindetails"""
"""Create Table name as userdatas"""
"""Create 6 Columns"""
"""
1. username
2. password
3. city
4. Moviename
5. seatname
6. Amount
"""


def scrsidb_connectione(x: tkinter.Tk) -> None:
    """Centers the window on the screen and sets its sidb_connectione."""
    width = x.winfo_screenwidth()
    height = x.winfo_screenheight()

    x_pos = (width - 600) // 2
    y_pos = (height - 400) // 2

    x.geometry(f"550x350+{x_pos}+{y_pos}")


## Button Styles ##
def button_style() -> dict:
    """Returns styling for standard buttons."""
    return {
        "font": ("Arial", 12, "bold"),
        "bd": 3,
        "width": 9,
        "height": 1,
        "activebackground": "yellow",
        "activeforeground": "black",
        "fg": "white",
        "bg": "orange",
        "relief": "groove",
    }


def button_style1() -> dict:
    """Returns styling for larger buttons."""
    return {
        "font": ("Arial", 12, "bold"),
        "bd": 1,
        "width": 15,
        "height": 10,
        "activebackground": "yellow",
        "activeforeground": "black",
        "fg": "white",
        "bg": "orange",
        "relief": "groove",
    }


def button_style2() -> dict:
    """Returns styling for medium-sidb_connectioned buttons with different colors."""
    return {
        "font": ("Arial", 10, "bold"),
        "bd": 2,
        "width": 14,
        "height": 1,
        "activebackground": "yellow",
        "activeforeground": "black",
        "fg": "black",
        "bg": "darkviolet",
        "relief": "groove",
    }


## Label Styles ##
def labeltext() -> tuple:
    """Returns font and screen width for labels."""
    label_font = ("Gill Sans", 20, "bold")
    label_width = main_screen.winfo_screenwidth()

    return label_font, label_width


## Hide Error Label in SignUp ##
def hide_error_label() -> None:
    """Hides the error label in the SignUp window."""
    error_label.pack_forget()


## Hide Error Label in Login ##
def hide_error_label1() -> None:
    """Hides the error label in the Login window."""
    error_label1.pack_forget()


## Registration or SignUp Setup ##
def reg() -> None:
    """Sets up the registration screen with input fields and buttons."""
    global screen
    screen = tkinter.Toplevel(main_screen)
    if "screen" in globals():
        main_screen.withdraw()

    screen.title("REGISTER")
    scrsidb_connectione(screen)
    screen.configure(bg="black")

    global usn_verify
    global password
    global show_password
    global entry_password

    usn_verify = tkinter.StringVar()
    password = tkinter.StringVar()
    show_password = BooleanVar(value=False)

    label_font, label_width = labeltext()

    l1 = tkinter.Label(
        screen,
        text="Enter Your SignUp Details",
        bg="royalblue",
        fg="black",
        height="2",
        font=label_font,
        width=label_width,
    )
    l1.pack(pady=10)

    tkinter.Label(
        screen,
        text="Enter Your Username",
        font=("Gill Sans", 14, "bold"),
        bg="black",
        fg="white",
        height="2",
        width="30",
    ).pack()

    tkinter.Entry(screen, textvariable=usn_verify, width="20", font=("Gill Sans", 14)).pack()

    tkinter.Label(
        screen,
        text="Enter Your Password",
        font=("Gill Sans", 14, "bold"),
        bg="black",
        fg="white",
        height="2",
        width="30",
    ).pack()

    entry_password = tkinter.Entry(
        screen, textvariable=password, show="*", width="20", font=("Gill Sans", 14)
    )
    entry_password.pack(pady=2)

    toggle_button = Checkbutton(
        screen, text="Show Password", variable=show_password, command=toggle_password
    )
    toggle_button.pack(pady=10)

    tkinter.Button(screen, text="Sign Up", **button_style(), command=signed).pack()

    reopen_button = tkinter.Button(
        screen,
        text="Back",
        font=("Arial", 9, "bold"),
        width=8,
        height=1,
        bd=1,
        bg="black",
        fg="white",
        activebackground="yellow",
        activeforeground="black",
        command=back1,
    )

    reopen_button.place(relx=1.0, anchor="ne", x=-10, y=30)


def back1() -> None:
    """Returns to the main screen and hides the registration or login window."""
    main_screen.deiconify()
    if "screen" in globals():
        screen.withdraw()
    elif "login_screen" in globals():
        login_screen.withdraw()


## Toggle password visibility (SignUp) ##
def toggle_password() -> None:
    """Toggles the visibility of the password (either hidden or visible)."""
    if show_password.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="*")


## Handle SignUp submission ##
def signed() -> None:
    """Handles the registration data input and adds it to the database."""
    pwd_info = password.get()

    if len(usn_verify.get()) < 6 or len(pwd_info) < 6:
        global error_label
        error_label = tkinter.Label(
            screen,
            text="Username and Password must be at least 6 characters long",
            bg="black",
            fg="red",
        )
        error_label.pack(pady=2)
        screen.after(2500, hide_error_label)
    else:
        db_connection = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="logindetails"
        )
        mycursor = db_connection.cursor()

        sql = "INSERT INTO userdatas(username,password) VALUES(%s,%s)"
        val = (usn_verify.get(), pwd_info)

        try:
            mycursor.execute(sql, val)
            db_connection.commit()
            tkinter.Label(screen, text="Signed Up Successfully", bg="black", fg="Yellow").pack()
            print("\nSigned Up Successfully")
        except:
            db_connection.rollback()
        finally:
            print("\nWelcome to Film Buff\n")
            selectcity()
            mycursor.close()
            db_connection.close()
            if "screen" in globals():
                screen.withdraw()


## Login screen ##
def login() -> None:
    """Creates the login window with user input fields."""
    global login_screen
    login_screen = tkinter.Toplevel(main_screen)
    if "login_screen" in globals():
        main_screen.withdraw()

    login_screen.title("Login")
    scrsidb_connectione(login_screen)
    login_screen.configure(bg="black")

    global usn_verify
    global pwd_verify
    global show_password1
    global entry_password1

    usn_verify = tkinter.StringVar()
    pwd_verify = tkinter.StringVar()
    show_password1 = tkinter.BooleanVar(value=False)

    label_font, label_width = labeltext()

    l2 = tkinter.Label(
        login_screen,
        text="Enter Your Login Details",
        bg="darkviolet",
        fg="black",
        height="2",
        font=label_font,
        width=label_width,
    )
    l2.pack(pady=10)

    tkinter.Label(
        login_screen,
        text="Username",
        font=("Gill Sans", 14, "bold"),
        bg="black",
        fg="white",
        height="2",
        width="30",
    ).pack()

    tkinter.Entry(
        login_screen, textvariable=usn_verify, width="20", font=("Gill Sans", 14)
    ).pack()

    tkinter.Label(
        login_screen,
        text="Password",
        font=("Gill Sans", 14, "bold"),
        bg="black",
        fg="white",
        height="2",
        width="30",
    ).pack()

    entry_password1 = tkinter.Entry(
        login_screen,
        textvariable=pwd_verify,
        show="*",
        width="20",
        font=("Gill Sans", 14),
    )
    entry_password1.pack(pady=2)

    toggle_button1 = tkinter.Checkbutton(
        login_screen,
        text="Show Password",
        variable=show_password1,
        command=toggle_password1,
        bg="aquamarine",
    )
    toggle_button1.pack(pady=10)

    tkinter.Button(login_screen, text="Sign In", **button_style(), command=submit).pack()

    reopen_button1 = tkinter.Button(
        login_screen,
        text="Back",
        font=("Arial", 9, "bold"),
        width=8,
        height=1,
        bd=1,
        bg="black",
        fg="white",
        activebackground="yellow",
        activeforeground="black",
        command=back2,
    )
    reopen_button1.place(relx=1.0, anchor="ne", x=-10, y=30)


## Return to the main screen from login ##
def back2() -> None:
    """Returns to the main screen and hides the login window."""
    main_screen.deiconify()
    login_screen.withdraw()


## Toggle password visibility (Login) ##
def toggle_password1() -> None:
    """Toggles the visibility of the password in the login window."""
    if show_password1.get():
        entry_password1.config(show="")
    else:
        entry_password1.config(show="*")


## Handle login submission ##
def submit() -> None:
    """Verifies login credentials and logs the user in."""
    if len(usn_verify.get()) < 6 or len(pwd_verify.get()) < 6:
        global error_label1
        error_label1 = tkinter.Label(
            login_screen,
            text="Username and Password must be at least 6 characters long",
            bg="black",
            fg="red",
        )
        error_label1.pack(pady=2)
        login_screen.after(2500, hide_error_label1)
    else:
        db_connection1 = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="logindetails"
        )
        mycursor = db_connection1.cursor()
        mycursor.execute(
            "SELECT * FROM userdatas WHERE username=%s AND password=%s",
            (usn_verify.get(), pwd_verify.get()),
        )
        if mycursor.fetchone():
            tkinter.Label(
                login_screen, text="Login Successfully", bg="black", fg="Yellow"
            ).pack()
            selectcity()
            print("\nLogin Successfully")
            print("\nWelcome to Film Buff\n")
            mycursor.close()
            db_connection1.close()
            if "login_screen" in globals():
                login_screen.withdraw()
        else:
            tm.showerror("Error", "Invalid Username or Password")


## Select city after login ##
def selectcity() -> None:
    """Opens a window to select a city after successful login."""
    global city, lbl_text
    city = tkinter.Toplevel(main_screen)

    if "screen" in globals():
        screen.withdraw()
    elif "login_screen" in globals():
        login_screen.withdraw()

    city.title("Select City & Movie")
    scrsidb_connectione(city)
    city.configure(bg="black")

    label_font, label_width = labeltext()

    lbl_text = tkinter.StringVar()
    lbl_text.set("Select Your City")

    label = tkinter.Label(
        city,
        textvariable=lbl_text,
        height=1,
        width=label_width,
        font=label_font,
        bg="skyblue",
        fg="black",
    )
    label.pack()

    cities = [
        "Madurai",
        "Chennai",
        "Thirunelveli",
        "Coimbatore",
        "Salem",
        "Tiruchirappalli",
        "Nagercoil",
        "Thanjavur",
        "Pallavaram",
        "Erode",
        "Dindigul",
        "Ooty",
        "Kodaikanal",
        "Kanchipuram",
        "Puducherry",
        "Rameswaram",
        "Vellore",
        "Pudukkottai",
        "Tenkasi",
    ]

    global sc
    sc = tkinter.StringVar()
    sc.set("Cities")

    font_config = ("bold", 14)
    width_config = 15
    height_config = 1

    menubutton = tkinter.Menubutton(
        city,
        textvariable=sc,
        font=font_config,
        width=width_config,
        height=height_config,
        bd=0,
        bg="adb_connectionure",
        fg="black",
        activebackground="yellow",
        activeforeground="black",
    )

    menubutton.menu = tkinter.Menu(
        menubutton,
        tearoff=0,
        bd=0,
        bg="white",
        fg="black",
        activebackground="yellow",
        activeforeground="black",
        font=font_config,
    )
    menubutton["menu"] = menubutton.menu

    for city_name in cities:
        menubutton.menu.add_radiobutton(
            label=city_name,
            variable=sc,
            value=city_name,
            command=lambda: print_ans(lbl_text, menubutton, label, city),
        )
    menubutton.pack()
    label.pack()

    movies_list(city)

    reopen_button2 = tkinter.Button(
        city,
        text="Sign Out",
        font=("Arial", 9, "bold"),
        width=8,
        height=1,
        bd=1,
        bg="dimgrey",
        fg="white",
        activebackground="yellow",
        activeforeground="black",
        command=lambda: signout(city),
    )
    reopen_button2.place(relx=1.0, anchor="ne", x=-10, y=8)
    reopen_button2.lift()


## Logout and return to main screen ##
def signout(city: tkinter.Toplevel) -> None:
    """Logs out and returns to the main screen."""
    main_screen.deiconify()
    if "screen" in globals():
        screen.withdraw()
    elif "login_screen" in globals():
        login_screen.destroy()
    city.withdraw()


def movies_list(city: tkinter.Toplevel) -> None:
    """Displays a list of movie buttons for selection, which leads to seat selection."""

    btn1 = tkinter.Button(
        city,
        text="Movie 1",
        **button_style1(),
        command=lambda: seat_selection(city, "Movie 1"),
    )
    btn1.pack(side=tkinter.LEFT, padx=15, pady=10, anchor=tkinter.CENTER)

    btn2 = tkinter.Button(
        city,
        text="Movie 2",
        **button_style1(),
        command=lambda: seat_selection(city, "Movie 2"),
    )
    btn2.pack(side=LEFT, padx=15, pady=10, anchor=CENTER)

    btn3 = Button(
        city,
        text="Movie 3",
        **button_style1(),
        command=lambda: seat_selection(city, "Movie 3"),
    )
    btn3.pack(side=tkinter.LEFT, padx=15, pady=10, anchor=tkinter.CENTER)


def seat_selection(city: tkinter.Toplevel, movie_name_fetch: str) -> None:
    """
    Displays seat selection options for a selected movie.
    """
    global seat, movie_name
    seat = tkinter.Toplevel(city)
    if "city" in globals():
        city.withdraw()
    movie_name = movie_name_fetch

    global s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12
    global s13, s14, s15, s16,s17, s18, s19, s20, s21, s22
    global s23, s24, s25, s26, s27, s28, s29, s30, s31, s32
    global s34, s35, s36, s37, s38, s39, s40, s41, s42, s33
    global s43, s44, s45, s46, s47, s48, s49, s50, s51, s52
    global s53, s54, s55, s56, s57, s58, s59, s60, s61, s62
    global s63, s64, s65, s66, s67, s68, s69, s70, s71, s72
    global s73, s74, s75, s76, s77, s78, s79, s80, s81, s82
    global s83, s84, s85, s86, s87, s88, s89, s90
    global s91, s92, s93, s94, s95, s96

    s1 = tkinter.IntVar()
    s2 = tkinter.IntVar()
    s3 = tkinter.IntVar()
    s4 = tkinter.IntVar()
    s5 = tkinter.IntVar()
    s6 = tkinter.IntVar()
    s7 = tkinter.IntVar()
    s8 = tkinter.IntVar()
    s9 = tkinter.IntVar()
    s10 = tkinter.IntVar()
    s11 = tkinter.IntVar()
    s12 = tkinter.IntVar()
    s13 = tkinter.IntVar()
    s14 = tkinter.IntVar()
    s15 = tkinter.IntVar()
    s16 = tkinter.IntVar()
    s17 = tkinter.IntVar()
    s18 = tkinter.IntVar()
    s19 = tkinter.IntVar()
    s20 = tkinter.IntVar()
    s21 = tkinter.IntVar()
    s22 = tkinter.IntVar()
    s23 = tkinter.IntVar()
    s24 = tkinter.IntVar()
    s25 = tkinter.IntVar()
    s26 = tkinter.IntVar()
    s27 = tkinter.IntVar()
    s28 = tkinter.IntVar()
    s29 = tkinter.IntVar()
    s30 = tkinter.IntVar()
    s31 = tkinter.IntVar()
    s32 = tkinter.IntVar()
    s33 = tkinter.IntVar()
    s34 = tkinter.IntVar()
    s35 = tkinter.IntVar()
    s36 = tkinter.IntVar()
    s37 = tkinter.IntVar()
    s38 = tkinter.IntVar()
    s39 = tkinter.IntVar()
    s40 = tkinter.IntVar()
    s41 = tkinter.IntVar()
    s42 = tkinter.IntVar()
    s43 = tkinter.IntVar()
    s44 = tkinter.IntVar()
    s45 = tkinter.IntVar()
    s46 = tkinter.IntVar()
    s47 = tkinter.IntVar()
    s48 = tkinter.IntVar()
    s49 = tkinter.IntVar()
    s50 = tkinter.IntVar()
    s51 = tkinter.IntVar()
    s52 = tkinter.IntVar()
    s53 = tkinter.IntVar()
    s54 = tkinter.IntVar()
    s55 = tkinter.IntVar()
    s56 = tkinter.IntVar()
    s57 = tkinter.IntVar()
    s58 = tkinter.IntVar()
    s59 = tkinter.IntVar()
    s60 = tkinter.IntVar()
    s61 = tkinter.IntVar()
    s62 = tkinter.IntVar()
    s63 = tkinter.IntVar()
    s64 = tkinter.IntVar()
    s65 = tkinter.IntVar()
    s66 = tkinter.IntVar()
    s67 = tkinter.IntVar()
    s68 = tkinter.IntVar()
    s69 = tkinter.IntVar()
    s70 = tkinter.IntVar()
    s71 = tkinter.IntVar()
    s72 = tkinter.IntVar()
    s73 = tkinter.IntVar()
    s74 = tkinter.IntVar()
    s75 = tkinter.IntVar()
    s76 = tkinter.IntVar()
    s77 = tkinter.IntVar()
    s78 = tkinter.IntVar()
    s79 = tkinter.IntVar()
    s80 = tkinter.IntVar()
    s81 = tkinter.IntVar()
    s82 = tkinter.IntVar()
    s83 = tkinter.IntVar()
    s84 = tkinter.IntVar()
    s85 = tkinter.IntVar()
    s86 = tkinter.IntVar()
    s87 = tkinter.IntVar()
    s88 = tkinter.IntVar()
    s89 = tkinter.IntVar()
    s90 = tkinter.IntVar()
    s91 = tkinter.IntVar()
    s92 = tkinter.IntVar()
    s93 = tkinter.IntVar()
    s94 = tkinter.IntVar()
    s95 = tkinter.IntVar()
    s96 = tkinter.IntVar()

    scrsidb_connectione(seat)

    seat.title("Seat Selection")
    seat.configure(bg="black")

    label_font, label_width = labeltext()

    label_0 = tkinter.Label(
        seat, text="SELECT YOUR SEATS", width=label_width, font=label_font
    ).pack()

    reopen_btn1 = tkinter.Button(
        seat,
        text="Back",
        font=("Arial", 9, "bold"),
        width=7,
        height=1,
        bd=1,
        bg="black",
        fg="white",
        activebackground="yellow",
        activeforeground="black",
        command=back_1,
    )

    reopen_btn1.place(relx=1.0, anchor="ne", x=-10, y=8)

    reopen_btn2 = tkinter.Button(
        seat,
        text="LogOut",
        font=("Arial", 9, "bold"),
        width=8,
        height=1,
        bd=1,
        bg="black",
        fg="white",
        activebackground="yellow",
        activeforeground="black",
        command=signout_1,
    )

    reopen_btn2.place(relx=0.0, anchor="nw", x=10, y=8)

    # Row A#
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s1,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=50, y=65)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s2,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=80, y=65)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s3,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=110, y=65)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s4,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=140, y=65)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s5,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=170, y=65)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s6,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=200, y=65)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s7,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=230, y=65)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s8,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=260, y=65)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s9,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=290, y=65)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s10,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=320, y=65)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s11,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=350, y=65)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s12,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=380, y=65)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s13,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=410, y=65)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s14,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=440, y=65)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s15,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=470, y=65)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s16,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=500, y=65)

    # Row B#
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s17,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=50, y=95)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s18,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=80, y=95)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s19,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=110, y=95)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s20,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=140, y=95)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s21,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=170, y=95)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s22,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=200, y=95)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s23,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=230, y=95)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s24,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=260, y=95)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s25,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=290, y=95)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s26,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=320, y=95)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s27,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=350, y=95)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s28,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=380, y=95)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s29,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=410, y=95)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s30,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=440, y=95)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s31,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=470, y=95)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s32,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=500, y=95)

    # Row C#
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s33,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=50, y=125)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s34,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=80, y=125)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s35,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=110, y=125)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s36,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=140, y=125)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s37,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=170, y=125)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s38,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=200, y=125)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s39,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=230, y=125)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s40,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=260, y=125)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s41,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=290, y=125)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s42,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=320, y=125)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s43,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=350, y=125)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s44,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=380, y=125)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s45,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=410, y=125)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s46,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=440, y=125)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s47,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=470, y=125)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s48,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=500, y=125)

    # Row D#
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s49,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=50, y=155)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s50,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=80, y=155)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s51,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=110, y=155)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s52,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=140, y=155)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s53,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=170, y=155)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s54,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=200, y=155)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s55,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=230, y=155)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s56,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=260, y=155)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s57,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=290, y=155)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s58,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=320, y=155)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s59,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=350, y=155)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s60,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=380, y=155)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s61,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=410, y=155)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s62,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=440, y=155)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s63,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=470, y=155)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s64,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=500, y=155)

    # Row E#
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s65,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=50, y=185)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s66,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=80, y=185)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s67,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=110, y=185)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s68,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=140, y=185)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s69,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=170, y=185)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s70,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=200, y=185)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s71,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=230, y=185)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s72,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=260, y=185)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s73,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=290, y=185)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s74,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=320, y=185)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s75,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=350, y=185)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s76,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=380, y=185)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s77,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=410, y=185)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s78,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=440, y=185)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s79,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=470, y=185)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s80,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=500, y=185)

    # Row F#
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s81,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=50, y=215)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s82,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=80, y=215)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s83,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=110, y=215)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s84,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=140, y=215)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s85,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=170, y=215)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s86,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=200, y=215)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s87,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=230, y=215)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s88,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=260, y=215)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s89,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=290, y=215)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s90,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=320, y=215)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s91,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=350, y=215)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s92,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=380, y=215)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s93,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=410, y=215)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s94,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=440, y=215)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s95,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=470, y=215)
    tkinter.Checkbutton(
        seat,
        text="",
        onvalue=1,
        offvalue=0,
        height=2,
        variable=s96,
        bg="grey",
        fg="black",
        activebackground="darkviolet",
        activeforeground="black",
    ).place(x=500, y=215)

    tkinter.Label(
        seat, text="Screen", bg="black", fg="darkviolet", font=("Gill Sans", 9, "bold")
    ).place(x=255, y=265)
    canvas = Canvas(seat, width=200, height=10, bg="lightcyan")
    canvas.place(x=180, y=285)
    rect_width = 350
    rect_height = 100
    # seat selection #
    tkinter.Button(
        seat, text="Confirm Booking", **button_style2(), command=seat_confirmation
    ).pack(side=tkinter.BOTTOM)

    font_new = ("Gill Sans", 12, "bold")

    tkinter.Label(seat, text="A", bg="black", fg="darkviolet",
     font=font_new).place(x=10, y=70)
    tkinter.Label(seat, text="B", bg="black", fg="darkviolet",
     font=font_new).place(x=10, y=100)
    tkinter.Label(seat, text="C", bg="black", fg="darkviolet",
     font=font_new).place(x=10, y=130)
    tkinter.Label(seat, text="D", bg="black", fg="darkviolet",
     font=font_new).place(x=10, y=160)
    tkinter.Label(seat, text="E", bg="black", fg="darkviolet",
     font=font_new).place(x=10, y=190)
    tkinter.Label(seat, text="F", bg="black", fg="darkviolet",
     font=font_new).place(x=10, y=220)

    tkinter.Label(seat, text="1", bg="black", fg="darkviolet",
     font=font_new).place(x=52, y=40)
    tkinter.Label(seat, text="2", bg="black", fg="darkviolet",
     font=font_new).place(x=82, y=40)
    tkinter.Label(seat, text="3", bg="black", fg="darkviolet", font=font_new).place(x=112, y=40)
    tkinter.Label(seat, text="4", bg="black", fg="darkviolet",
     font=font_new).place(x=142, y=40)
    tkinter.Label(seat, text="5", bg="black", fg="darkviolet",
     font=font_new).place(x=172, y=40)
    tkinter.Label(seat, text="6", bg="black", fg="darkviolet",
     font=font_new).place(x=202, y=40)
    tkinter.Label(seat, text="7", bg="black", fg="darkviolet",
     font=font_new).place(x=232, y=40)
    tkinter.Label(seat, text="8", bg="black", fg="darkviolet",
     font=font_new).place(x=262, y=40)
    tkinter.Label(seat, text="9", bg="black", fg="darkviolet",
     font=font_new).place(x=292, y=40)
    tkinter.Label(seat, text="10", bg="black", fg="darkviolet",
     font=font_new).place(
        x=320, y=40
    )
    tkinter.Label(seat, text="11", bg="black", fg="darkviolet",
     font=font_new).place(
        x=350, y=40
    )
    tkinter.Label(seat, text="12", bg="black", fg="darkviolet",
     font=font_new).place(
        x=380, y=40
    )
    tkinter.Label(seat, text="13", bg="black", fg="darkviolet",
     font=font_new).place(
        x=410, y=40
    )
    tkinter.Label(seat, text="14", bg="black", fg="darkviolet",
     font=font_new).place(
        x=440, y=40
    )
    tkinter.Label(seat, text="15", bg="black", fg="darkviolet",
     font=font_new).place(
        x=470, y=40
    )
    tkinter.Label(seat, text="16", bg="black", fg="darkviolet",
     font=font_new).place(
        x=500, y=40
    )

    seat.mainloop()


def seat_confirmation():
    global seat_name, Amount
    seat_name = ""
    Amount = 0

    if s1.get() == 1:
        seat_name += "A1,"
        Amount += 190

    if s2.get() == 1:
        seat_name += "A2,"
        Amount += 190

    if s3.get() == 1:
        seat_name += "A3,"
        Amount += 190

    if s4.get() == 1:
        seat_name += "A4,"
        Amount += 190

    if s5.get() == 1:
        seat_name += "A5,"
        Amount += 190

    if s6.get() == 1:
        seat_name += "A6,"
        Amount += 190

    if s7.get() == 1:
        seat_name += "A7,"
        Amount += 190

    if s8.get() == 1:
        seat_name += "A8,"
        Amount += 190

    if s9.get() == 1:
        seat_name += "A9,"
        Amount += 190

    if s10.get() == 1:
        seat_name += "A10,"
        Amount += 190

    if s11.get() == 1:
        seat_name += "A11,"
        Amount += 190

    if s12.get() == 1:
        seat_name += "A12,"
        Amount += 190

    if s13.get() == 1:
        seat_name += "A13,"
        Amount += 190

    if s14.get() == 1:
        seat_name += "A14,"
        Amount += 190

    if s15.get() == 1:
        seat_name += "A15,"
        Amount += 190

    if s16.get() == 1:
        seat_name += "A16,"
        Amount += 190
    ###################################
    if s17.get() == 1:
        seat_name += "B1,"
        Amount += 190

    if s18.get() == 1:
        seat_name += "B2,"
        Amount += 190

    if s19.get() == 1:
        seat_name += "B3,"
        Amount += 190

    if s20.get() == 1:
        seat_name += "B4,"
        Amount += 190

    if s21.get() == 1:
        seat_name += "B5,"
        Amount += 190

    if s22.get() == 1:
        seat_name += "B6,"
        Amount += 190

    if s23.get() == 1:
        seat_name += "B7,"
        Amount += 190

    if s24.get() == 1:
        seat_name += "B8,"
        Amount += 190

    if s25.get() == 1:
        seat_name += "B9,"
        Amount += 190

    if s26.get() == 1:
        seat_name += "B10,"
        Amount += 190

    if s27.get() == 1:
        seat_name += "B11,"
        Amount += 190

    if s28.get() == 1:
        seat_name += "B12,"
        Amount += 190

    if s29.get() == 1:
        seat_name += "B13,"
        Amount += 190

    if s30.get() == 1:
        seat_name += "B14,"
        Amount += 190

    if s31.get() == 1:
        seat_name += "B15,"
        Amount += 190

    if s32.get() == 1:
        seat_name += "B16,"
        Amount += 190
    ####################################
    if s33.get() == 1:
        seat_name += "C1,"
        Amount += 190

    if s34.get() == 1:
        seat_name += "C2,"
        Amount += 190

    if s35.get() == 1:
        seat_name += "C3,"
        Amount += 190

    if s36.get() == 1:
        seat_name += "C4,"
        Amount += 190

    if s37.get() == 1:
        seat_name += "C5,"
        Amount += 190

    if s38.get() == 1:
        seat_name += "C6,"
        Amount += 190

    if s39.get() == 1:
        seat_name += "C7,"
        Amount += 190

    if s40.get() == 1:
        seat_name += "C8,"
        Amount += 190

    if s41.get() == 1:
        seat_name += "C9,"
        Amount += 190

    if s42.get() == 1:
        seat_name += "C10,"
        Amount += 190

    if s43.get() == 1:
        seat_name += "C11,"
        Amount += 190

    if s44.get() == 1:
        seat_name += "C12,"
        Amount += 190

    if s45.get() == 1:
        seat_name += "C13,"
        Amount += 190

    if s46.get() == 1:
        seat_name += "C14,"
        Amount += 190

    if s47.get() == 1:
        seat_name += "C15,"
        Amount += 190

    if s48.get() == 1:
        seat_name += "C16,"
        Amount += 190
    ##########################################
    if s49.get() == 1:
        seat_name += "D1,"
        Amount += 190

    if s50.get() == 1:
        seat_name += "D2,"
        Amount += 190

    if s51.get() == 1:
        seat_name += "D3,"
        Amount += 190

    if s52.get() == 1:
        seat_name += "D4,"
        Amount += 190

    if s53.get() == 1:
        seat_name += "D5,"
        Amount += 190

    if s54.get() == 1:
        seat_name += "D6,"
        Amount += 190

    if s55.get() == 1:
        seat_name += "D7,"
        Amount += 190

    if s56.get() == 1:
        seat_name += "D8,"
        Amount += 190

    if s57.get() == 1:
        seat_name += "D9,"
        Amount += 190

    if s58.get() == 1:
        seat_name += "D10,"
        Amount += 190

    if s59.get() == 1:
        seat_name += "D11,"
        Amount += 190

    if s60.get() == 1:
        seat_name += "D12,"
        Amount += 190

    if s61.get() == 1:
        seat_name += "D13,"
        Amount += 190

    if s62.get() == 1:
        seat_name += "D14,"
        Amount += 190

    if s63.get() == 1:
        seat_name += "D15,"
        Amount += 190

    if s64.get() == 1:
        seat_name += "D16,"
        Amount += 190
    ###################################
    if s65.get() == 1:
        seat_name += "E1,"
        Amount += 190

    if s66.get() == 1:
        seat_name += "E2,"
        Amount += 190

    if s67.get() == 1:
        seat_name += "E3,"
        Amount += 190

    if s68.get() == 1:
        seat_name += "E4,"
        Amount += 190

    if s69.get() == 1:
        seat_name += "E5,"
        Amount += 190

    if s70.get() == 1:
        seat_name += "E6,"
        Amount += 190

    if s71.get() == 1:
        seat_name += "E7,"
        Amount += 190

    if s72.get() == 1:
        seat_name += "E8,"
        Amount += 190

    if s73.get() == 1:
        seat_name += "E9,"
        Amount += 190

    if s74.get() == 1:
        seat_name += "E10,"
        Amount += 190

    if s75.get() == 1:
        seat_name += "E11,"
        Amount += 190

    if s76.get() == 1:
        seat_name += "E12,"
        Amount += 190

    if s77.get() == 1:
        seat_name += "E13,"
        Amount += 190

    if s78.get() == 1:
        seat_name += "E14,"
        Amount += 190

    if s79.get() == 1:
        seat_name += "E15,"
        Amount += 190

    if s80.get() == 1:
        seat_name += "E16,"
        Amount += 190
    ####################################
    if s81.get() == 1:
        seat_name += "F1,"
        Amount += 190

    if s82.get() == 1:
        seat_name += "F2,"
        Amount += 190

    if s83.get() == 1:
        seat_name += "F3,"
        Amount += 190

    if s84.get() == 1:
        seat_name += "F4,"
        Amount += 190

    if s85.get() == 1:
        seat_name += "F5,"
        Amount += 190

    if s86.get() == 1:
        seat_name += "F6,"
        Amount += 190

    if s87.get() == 1:
        seat_name += "F7,"
        Amount += 190

    if s88.get() == 1:
        seat_name += "F8,"
        Amount += 190

    if s89.get() == 1:
        seat_name += "F9,"
        Amount += 190

    if s90.get() == 1:
        seat_name += "F10,"
        Amount += 190

    if s91.get() == 1:
        seat_name += "F11,"
        Amount += 190

    if s92.get() == 1:
        seat_name += "F12,"
        Amount += 190

    if s93.get() == 1:
        seat_name += "F13,"
        Amount += 190

    if s94.get() == 1:
        seat_name += "F14,"
        Amount += 190

    if s95.get() == 1:
        seat_name += "F15,"
        Amount += 190

    if s96.get() == 1:
        seat_name += "F16,"
        Amount += 190
    ##########################################

    updating_values(seat)


def back_1() -> None:
    """Show the city window and hide the seat window."""
    city.deiconify()
    seat.withdraw()


def signout_1() -> None:
    """Show the main screen and hide the current screen."""
    main_screen.deiconify()
    if "screen" in globals():
        screen.withdraw()
    elif "login_screen" in globals():
        login_screen.withdraw()
    city.withdraw()
    seat.withdraw()


def updating_values(seat: Tk) -> None:
    """
    Update user data in the database with selected seat information.

    Parameters:
    seat (Tk): The parent window for the booking.
    """
    db_connection = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="logindetails"
    )

    mycursor = db_connection.cursor()
    sql1 = "UPDATE userdatas SET city='{}', Moviename='{}', seatname='{}'",
    " Amount='{}' WHERE username='{}'"
    val1 = sql1.format(lbl_text.get(), movie_name, seat_name,
     Amount, usn_verify.get())
    print(val1)

    try:
        print(lbl_text.get())
        print("Your Seats: " + seat_name)
        print("Total Cost: " + str(Amount))
        print(movie_name)
        mycursor.execute(val1)
        db_connection.commit()
        booking_successfully(seat)
    except:
        db_connection.rollback()
    finally:
        mycursor.close()
        db_connection.close()


def booking_successfully(seat: tkinter.Tk) -> None:
    """
    Display a success message for booked tickets.

    Parameters:
    seat (Tk): The parent window for the booking.
    """
    global booked, seat_name, Amount

    booked = tkinter.Toplevel(seat)
    if "seat" in globals():
        seat.withdraw()

    booked.title("Tickets")
    scrsidb_connectione(booked)
    booked.configure(bg="black")

    label_font, label_width = labeltext()

    tkinter.Label(
        booked,
        text="Tickets Booked Successfully",
        bg="pink",
        fg="black",
        height="2",
        font=label_font,
        width=label_width,
    ).pack()

    reopen_btn3 = tkinter.Button(
        booked,
        text="Back",
        font=("Arial", 9, "bold"),
        width=7,
        height=1,
        bd=1,
        bg="black",
        fg="white",
        activebackground="yellow",
        activeforeground="black",
        command=back_2,
    )
    reopen_btn3.place(relx=1.0, anchor="ne", x=-10, y=8)

    reopen_btn4 = tkinter.Button(
        booked,
        text="LogOut",
        font=("Arial", 9, "bold"),
        width=8,
        height=1,
        bd=1,
        bg="black",
        fg="white",
        activebackground="yellow",
        activeforeground="black",
        command=signout_2,
    )
    reopen_btn4.place(relx=0.0, anchor="nw", x=10, y=8)

    tkinter.Label(
        booked,
        text="Your Tickets\n~~~~~~~~~~~~~~",
        bg="black",
        fg="darkviolet",
        height="3",
        font=label_font,
        width=label_width,
    ).pack()

    seat_label = tkinter.Label(
        booked,
        text="Your Seats: " + seat_name,
        bg="yellow",
        fg="black",
        height="1",
        font=label_font,
    )
    seat_label.pack()

    cost_label = tkinter.Label(
        booked,
        text="Total Cost: " + str(Amount),
        bg="yellow",
        fg="black",
        height="1",
        font=label_font,
    )
    cost_label.pack()


def back_2() -> None:
    """Show the city window and hide the booking confirmation window."""
    city.deiconify()
    booked.withdraw()


def signout_2() -> None:
    """Show the main screen and hide all other windows."""
    main_screen.deiconify()
    if "screen" in globals():
        screen.withdraw()
    elif "login_screen" in globals():
        login_screen.withdraw()
    city.withdraw()
    seat.withdraw()
    booked.withdraw()


def print_ans(lbl_text, menubutton, label, city) -> None:
    """
    Display the selected city and update the menu button.

    Parameters:
    lbl_text: Label variable to display the city.
    menubutton: Button to change the city.
    label: Label to change the background color.
    city: The current city.
    """
    global scity
    scity = sc.get()
    print("Selected City: " + scity + "\n")
    lbl_text.set("Your City: " + scity)
    label.config(bg="orangered")

    global changecity
    changecity = tkinter.StringVar()
    changecity.set("Change\nYou're City")

    menubutton.config(
        textvariable=changecity,
        font=("Arial", 9, "bold"),
        width=8,
        height=1,
        bd=4,
        bg="pink",
        fg="black",
        activebackground="yellow",
        activeforeground="black",
    )

    x = label.winfo_x()
    y = label.winfo_y()

    menubutton.place(x=x + 5, y=y + 3)
    menubutton.lift()


def main_account_screen() -> None:
    """Initialidb_connectione and display the main account screen."""
    global main_screen
    main_screen = tkinter.Tk()

    scrsidb_connectione(main_screen)
    main_screen.configure(bg="black")

    label_font, label_width = labeltext()

    main_screen.title("Film Buff")
    tkinter.Label(
        main_screen,
        text="Film Buff",
        bg="yellow",
        fg="black",
        height="2",
        font=label_font,
        width=label_width,
    ).pack()
    tkinter.Label(main_screen, text="", bg="black").pack()

    btn = tkinter.Button(text="New User", command=reg, **button_style())
    btn.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    btn1 = tkinter.Button(text="Login", command=login, **button_style())
    btn1.place(relx=0.5, rely=0.6, anchor=N)

    main_screen.mainloop()


main_account_screen()

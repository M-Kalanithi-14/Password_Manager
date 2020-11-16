import tkinter as tk
from tkinter import messagebox
from sys import platform
try : import pymysql as cntr
except ImportError: import mysql.connector as cntr

if platform == "linux":
    db = cntr.connect(host="localhost", user='JB', passwd='manager', database="pasman")
else:
    db = cntr.connect(host="localhost", user='root', passwd='manager', database="pasman")

cur = db.cursor()

def MainWindow(LocUser):
    root = tk.Tk()
    root.title('Password Manager')
    #root.iconbitmap("icon.ico")
    root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0')
    #root.resizable(False,False)

    #============================== Variables ===============================
    LocUser = LocUser
    Website = tk.StringVar(root)
    Email = tk.StringVar(root)
    Username = tk.StringVar(root)
    Password = tk.StringVar(root)

    #============================== Functions =============================
    def disp() :
        cur.execute(f"select * from AccountDetails where user = '{LocUser}';")
        L1 = cur.fetchall()
        T1 = ()        
        if any(L1) : 
            for i in L1 :
                T1 += (f"{i[1]}\t\t\t\t\t {i[2]}\t\t\t\t\t {i[3]}\t\t\t\t\t {i[4]}\t\t\t\t\t\n" + '-'.center(316 , '-') + '\n',)
        return T1

    def ADD():
        if Website.get() == '' :
            txtWebsite.configure(bg = 'red' , fg = 'white')
            messagebox.showerror("Add New Details" , "You've left the Website field EMPTY!!!  All fields are MUST.")
        elif Email.get() == '' :
            txtEmail.configure(bg = 'red' , fg = 'white')
            messagebox.showerror("Add New Details" , "You've left the Email ID field EMPTY!!!  All fields are MUST.")
        elif Username.get() == '' :
            txtUsername.configure(bg = 'red' , fg = 'white')
            messagebox.showerror("Add New Details" , "You've left the Username field EMPTY!!!  All fields are MUST.")
        elif Password.get() == '' :
            txtPassword.configure(bg = 'red' , fg = 'white')
            messagebox.showerror("Add New Details" , "You've left the Password field EMPTY!!!  All fields are MUST.")
        else:
            cur.execute(f"insert into AccountDetails values('{LocUser}','{Website.get()}','{Email.get()}','{Username.get()}','{Password.get()}');")
            db.commit()
            messagebox.showinfo("Add New Details","Details have been SUCCESSFULLY Added!!!")            
            txtDetails.insert('end' , f'{Website.get()}\t\t\t\t\t {Email.get()}\t\t\t\t\t {Username.get()}\t\t\t\t\t {Password.get()}')
            txtDetails.insert('end' , ('-'.center(316 , '-') + '\n'))
            Website.set('')
            Email.set('')
            Username.set('')
            Password.set('')

    #============================== Frame Widgets ===========================
    Mainframe = tk.Frame(root)
    Mainframe.grid()

    Tops = tk.Frame(Mainframe , bd = 10 , relief = 'ridge')
    Tops.pack(side = 'top')

    lblTitle = tk.Label(Tops , width = 30 , font = ('arial' , 40 , 'bold') ,
                                text = 'Password Manager' , justify = 'center')
    lblTitle.grid(padx = 150)

    Membername = tk.LabelFrame(Mainframe , bd = 10 , width = 1300 , height = 300 ,
                                font = ('arial' , 12 , 'bold') , text = 'Add New Details' , relief = 'ridge')
    Membername.pack(padx = 38 , side = 'top')

    DetailsFrame = tk.LabelFrame(Mainframe , bd = 10 , width = 2000 , height = 200 ,
                                        font = ('arial' , 12 , 'bold') , text = 'Your Details' , relief = 'ridge')
    DetailsFrame.pack(padx = 38 , side = 'top')

    #============================== Label and Entry Widgets ===========================
    lblWebsite = tk.Label(Membername , font = ('arial' , 16 , 'bold') ,
                                text = 'Website URL' , bd = 7)
    lblWebsite.grid(row = 0 , column = 0 , sticky = 'n')        
    txtWebsite = tk.Entry(Membername , font = ('arial' , 13 , 'bold') ,
                                textvariable = Website , bd = 7 , insertwidth = 2)
    txtWebsite.grid(row = 0 , column = 1)

    lblEmail = tk.Label(Membername , font = ('arial' , 16 , 'bold') ,
                                text = 'Email ID' , bd = 7)
    lblEmail.grid(row = 1 , column = 0 , sticky = 'n')        
    txtEmail = tk.Entry(Membername , font = ('arial' , 13 , 'bold') ,
                                textvariable = Email , bd = 7 , insertwidth = 2)
    txtEmail.grid(row = 1 , column = 1)

    lblUsername = tk.Label(Membername , font = ('arial' , 16 , 'bold') ,
                                text = 'Username' , bd = 7)
    lblUsername.grid(row = 0 , column = 3 , sticky = 'n')        
    txtUsername = tk.Entry(Membername , font = ('arial' , 13 , 'bold') ,
                                textvariable = Username , bd = 7 , insertwidth = 2)
    txtUsername.grid(row = 0 , column = 4)

    lblPassword = tk.Label(Membername , font = ('arial' , 16 , 'bold') ,
                                text = 'Password' , bd = 7)
    lblPassword.grid(row = 1 , column = 3 , sticky = 'n')        
    txtPassword = tk.Entry(Membername , font = ('arial' , 13 , 'bold') , show='*',
                                textvariable = Password , bd = 7 , insertwidth = 2)
    txtPassword.grid(row = 1 , column = 4)

    btnPrint = tk.Button(Membername, bd = 5,
                                font = ('arial' , 16 , 'bold') , text = 'Add' , command = ADD)    
    btnPrint.grid(row = 1 , column = 5)

    #============================== Text Widget============================
    txtDetails = tk.Text(DetailsFrame , width = 181 , height = 20 , font = ('arial' , 10 , 'bold'))
    txtDetails.grid(row = 0 , column = 0 , columnspan = 4)
    txtDetails.insert('end' , ('-'.center(316 , '-') + '\n'))
    txtDetails.insert('end' , '     Website URLs\t\t\t\t\t       Email ID\t\t\t\t           Username\t\t\t\t\t\t Password\n')
    txtDetails.insert('end' , ('-'.center(316 , '-') + '\n'))
    for i in disp() :
        txtDetails.insert('end' , i)

    root.mainloop()

def register(root) :
    root.destroy()

    root_reg = tk.Tk()
    root_reg.title("Register")
    #root_reg.iconbitmap("icon.ico")
    root_reg.group()

    name = tk.StringVar(root_reg)
    Email = tk.StringVar(root_reg)
    username = tk.StringVar(root_reg)
    password = tk.StringVar(root_reg)
    password2 = tk.StringVar(root_reg)

    #===================================== Widgets ===============================
    lblName = tk.Label(root_reg , font = ('arial' , 16 , 'bold') ,
                           text = 'Enter Full Name : ')
    lblName.grid(row = 0 , column = 0)
    txtName  = tk.Entry(root_reg , font = ('arial' , 13 , 'bold') , bd = 7,
                            textvariable = name , insertwidth = 2)
    txtName.grid(row = 0 , column = 2)

    lblEmail = tk.Label(root_reg , font = ('arial' , 16 , 'bold') ,
                           text = 'Enter E-Mail ID : ')
    lblEmail.grid(row = 2 , column = 0)
    txtEmail = tk.Entry(root_reg , font = ('arial' , 13 , 'bold') , bd = 7,
                            textvariable = Email , insertwidth = 2)
    txtEmail.grid(row = 2 , column = 2)

    lblUsername = tk.Label(root_reg , font = ('arial' , 16 , 'bold') ,
                           text = 'Enter Username : ')
    lblUsername.grid(row = 4 , column = 0)
    txtUsername  = tk.Entry(root_reg , font = ('arial' , 13 , 'bold') , bd = 7,
                            textvariable = username , insertwidth = 2)
    txtUsername.grid(row = 4 , column = 2)

    lblPassword = tk.Label(root_reg , font = ('arial' , 16 , 'bold') ,
                           text = 'Enter Password : ')
    lblPassword.grid(row = 6 , column = 0)
    txtPassword  = tk.Entry(root_reg , font = ('arial' , 13 , 'bold') , bd = 7,
                            textvariable = password , insertwidth = 2 , show = '*')
    txtPassword.grid(row = 6 , column = 2)

    lblPassword2 = tk.Label(root_reg , font = ('arial' , 16 , 'bold') ,
                           text = 'Confirm Password : ')
    lblPassword2.grid(row = 8 , column = 0)
    txtPassword2 = tk.Entry(root_reg , font = ('arial' , 13 , 'bold') , bd = 7,
                            textvariable = password2 , insertwidth = 2 , show = '*')
    txtPassword2.grid(row = 8 , column = 2)

    #==================================== Inserting Data into MySQL ==============

    def reg() :
        if name.get() == '' :
            txtName.configure(bg = 'red' , fg = 'white')
            messagebox.showerror("Register" , "You've left the Name field EMPTY!!!  All fields are MUST.")
        elif Email.get() == '' :
            txtEmail.configure(bg = 'red' , fg = 'white')
            messagebox.showerror("Register" , "You've left the Email ID field EMPTY!!!  All fields are MUST.")
        elif '@' not in Email.get() :
            txtEmail.configure(bg = 'red' , fg = 'white')
            messagebox.showerror("Register" , "You've Entered an INVALID Email ID!!! Please Check it.")
        elif username.get() == '' :
            txtUsername.configure(bg = 'red' , fg = 'white')
            messagebox.showerror("Register" , "You've left the Username field EMPTY!!!  All fields are MUST.")
        elif password.get() == '' :
            txtPassword.configure(bg = 'red' , fg = 'white')
            messagebox.showerror("Register" , "You've left the Password field EMPTY!!!  All fields are MUST.")
        elif password2.get() == '' :
            txtPassword2.configure(bg = 'red' , fg = 'white')
            messagebox.showerror("Register" , "You've left the Password Confirmation field EMPTY!!!  All fields are MUST.")
        else :
            if password.get() == password2.get() :                
                cur.execute(f"insert into users values('{name.get()}' , '{Email.get()}' , '{username.get()}' , '{password.get()}');")
                db.commit()
                messagebox.showinfo("Register" , "You've been REGISTERED Successfully.")
                login(root_reg)                
            else : messagebox.showerror("Register" , "You've Entered DIFFERENT Passwords!!")

    def Exit() :
        iExit = messagebox.askyesno('Register' , 'Do you want to quit ?')
        if iExit > 0 :
            root_reg.destroy()
            return

    def back() :
        root_reg.destroy()
        main()

    #==================================== Buttons ================================

    btnBack = tk.Button(root_reg , font=('arial', 16, 'bold'), text='<< Go Back' , command = back , bd = 7)
    btnBack.grid(row = 10 , column=0)

    btnRegister = tk.Button(root_reg , font=('arial', 16, 'bold'),
                         text='Register' , command = reg , bd = 7)
    btnRegister.grid(row=10, column=2)

    btnExit = tk.Button(root_reg , font=('arial', 16, 'bold'), text='Exit' , command = Exit , bd = 7)
    btnExit.grid(row = 10, column = 4)

    root_reg.mainloop()

#=================================================================================

def login(root) :
    root.destroy()

    root_login = tk.Tk()
    root_login.title("Login")
    #root_login.iconbitmap("icon.ico")
    root_login.group()


    username = tk.StringVar(root_login)
    password = tk.StringVar(root_login)

    #====================================== Widgets ==============================

    lblUsername = tk.Label(root_login , font = ('arial' , 16 , 'bold') ,
                           text = 'Enter Username')
    lblUsername.grid(row = 0 , column = 0)
    txtUsername  = tk.Entry(root_login , font = ('arial' , 13 , 'bold') , bd = 7,
                            textvariable = username , insertwidth = 2)
    txtUsername.grid(row = 0 , column = 2)

    lblPassword = tk.Label(root_login , font = ('arial' , 16 , 'bold') ,
                           text = 'Enter Password')
    lblPassword.grid(row = 2 , column = 0)
    txtPassword  = tk.Entry(root_login , font = ('arial' , 13 , 'bold') , bd = 7,
                            textvariable = password , insertwidth = 2 , show = '*')
    txtPassword.grid(row = 2 , column = 2)

    #==================================== Fetching Data from MySQL ===============

    def LOGIN() :
        if username.get() == '' :
            txtUsername.configure(bg = 'red' , fg = 'white')
            messagebox.showerror("Login" , "You've left the Username field EMPTY!!!  All fields are MUST.")
        elif password.get() == '' :
            txtPassword.configure(bg = 'red' , fg = 'white')
            messagebox.showerror("Login" , "You've left the Password field EMPTY!!!  All fields are MUST.")
        else :
            cur.execute(f"select * from users where username = '{username.get()}' and password = '{password.get()}';")
            L1 = cur.fetchall()
            if any(L1) :                
                root_login.destroy()
                MainWindow(username.get())
            else : messagebox.showerror("Login" , "Such a User DOESNOT Exist!!\nPlease Check whether the Entered Details are correct or not;\nor REGISTER Yourself")


    def Exit() :
        iExit = messagebox.askyesno('Login' , 'Do you want to quit ?')
        if iExit > 0 :
            root_login.destroy()
            return

    def back() :
        root_login.destroy()
        main()

    #==================================== Buttons ================================

    btnBack = tk.Button(root_login , font=('arial', 16, 'bold'), text='<< Go Back' , command = back , bd = 7)
    btnBack.grid(row = 4 , column=0)

    btnLogin = tk.Button(root_login , font=('arial', 16, 'bold'), text='Login' , command = LOGIN , bd = 7)
    btnLogin.grid(row=4, column=2)

    btnExit = tk.Button(root_login , font=('arial', 16, 'bold'), text='Exit' , command = Exit , bd = 7)
    btnExit.grid(row = 4 , column = 4)
    
    root_login.mainloop()

#=================================================================================

def main() :
    root = tk.Tk()
    root.title("Book Shop Management")
    #root.iconbitmap("icon.ico")
    root.geometry("555x170")
    root.group()
    #root.configure(bgpic = 'icon.ico')

    #============================= Buttons and Widgets ===========================

    lbltitle = tk.Label(root , font = ('Times new Roman' , 24 , 'bold') ,
                           text = '                Welcome To')
    lbltitle.grid(row = 0 , column = 0)

    lbltitle2 = tk.Label(root , font = ('Times new Roman' , 24 , 'bold') ,
                           text = '                Password Manager\n')
    lbltitle2.grid(row = 1 , column = 0)

    btnRegister = tk.Button(root , font=('arial', 16, 'bold'), text='Register' , command = lambda : register(root) , bd = 7)
    btnRegister.grid(row = 2 , column = 0 , sticky = 'w')

    btnLogin = tk.Button(root , font=('arial', 16, 'bold'), text='Login' , command = lambda : login(root) ,
                         bd = 7 , width = 6)
    btnLogin.grid(row=2 , column=1 , sticky = 'w')

    root.mainloop()
main()
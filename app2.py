import tkinter
import tkinter.messagebox
import customtkinter
import pymysql

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #configure window
        self.title("TipTops All-in-one App")
        self.geometry(f"{1500}x{750}")
        self.minsize(1000, 750)

        #configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3, 4), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        #Main tabs
        self.tabview = customtkinter.CTkTabview(self, width=500, height=1000, corner_radius=25 )
        self.tabview.grid(row=0, column=1, padx=(20,20), pady=(20,20), sticky="nsew")        
        self.tabview.add("Pricing")
        self.tabview.add("Invoices")
        self.tabview.add("Scheduling")
        self.tabview.add("Account")

        #Sidebar frame
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=25)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Options", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        #invoices tab
        self.invoices_tabview = customtkinter.CTkTabview(self.tabview.tab("Invoices"), corner_radius = 25)
        self.invoices_tabview.place(x=0, y=0, relwidth=1, relheight=1)
        self.invoices_tabview.add("Jobs")
        self.invoices_tabview.add("New Job")

        #Scheduling Tab
        self.scheduling_tabview = customtkinter.CTkTabview(self.tabview.tab("Scheduling"), corner_radius = 25)
        self.scheduling_tabview.place(x=0, y=0, relwidth=1, relheight=1)
        self.scheduling_tabview.add("Screen Printing")
        self.scheduling_tabview.add("Embroidery")
        self.scheduling_tabview.add("Art")
        
        #Appearance Settings
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        #Account Tab
        self.account_tabview = customtkinter.CTkTabview(self.tabview.tab("Account"), corner_radius=25)
        self.account_tabview.place(x=0, y=0, relwidth=1, relheight=1)
        self.account_tabview.add("Login")
        self.account_tabview.add("Register")

        #Account form
        self.signup = customtkinter.CTkLabel(self.account_tabview.tab("Register"), text="Create Account", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.signup.grid( padx=25, pady = 10)
        nameentry = customtkinter.CTkEntry(self.account_tabview.tab("Register"), width=125, height= 25, corner_radius=10, placeholder_text="Name")
        nameentry.grid( padx=25, pady = 10, sticky = "nw")
        name = nameentry.get()
        userentry = customtkinter.CTkEntry(self.account_tabview.tab("Register"), width=125, height= 25, corner_radius=10, placeholder_text="User Name")
        userentry.grid( padx=25, pady = 10, sticky = "nw")
        user = userentry.get()
        passwentry = customtkinter.CTkEntry(self.account_tabview.tab("Register"), width=125, height= 25, corner_radius=10, placeholder_text="Password")
        passwentry.grid( padx=25, pady = 10, sticky = "nw")
        passw = passwentry.get()
        passwVerientry = customtkinter.CTkEntry(self.account_tabview.tab("Register"), width=125, height= 25, corner_radius=10, placeholder_text="Verify Password")
        passwVerientry.grid( padx=25, pady = 10, sticky = "nw")
        passwVeri = passwVerientry.get()
        emailentry = customtkinter.CTkEntry(self.account_tabview.tab("Register"), width=125, height= 25, corner_radius=10, placeholder_text="Email")
        emailentry.grid( padx=25, pady = 10, sticky = "nw")
        email = emailentry.get()
        signUpBtn=customtkinter.CTkButton(self.account_tabview.tab("Register"),width=125,height=25,corner_radius=10, text="Sign Up", command = lambda name=nameentry.get(), user=userentry.get(), email=emailentry.get(), passw=passwentry.get(), passwVeri=passwVerientry.get(): self.register(name, user, email, passw, passwVeri))        
        signUpBtn.grid(padx = 25, pady = 10, sticky = "nw")

        #Login Form
        self.login = customtkinter.CTkLabel(self.account_tabview.tab("Login"), text="Login", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login.grid( padx=25, pady = 10, sticky = "nw")
        loginUserentry = customtkinter.CTkEntry(self.account_tabview.tab("Login"), width=125, height= 25, corner_radius=10, placeholder_text="User")
        loginUserentry.grid( padx=25, pady = 10, sticky = "nw")
        loginUser= loginUserentry
        loginPasswentry = customtkinter.CTkEntry(self.account_tabview.tab("Login"), width=125, height= 25, corner_radius=10, placeholder_text="User")
        loginPasswentry.grid( padx=25, pady = 10, sticky = "nw")
        loginPassw = loginPasswentry
        loginBtn = customtkinter.CTkButton(self.account_tabview.tab("Login"), width=125, height= 25, corner_radius=10, text="Sign Up", command = lambda: self.log_in(loginUser, loginPassw)) 
        loginBtn.grid(padx = 25, pady = 10, sticky = "nw")

    def register(self, name, user, email, passw, passwVeri):
        print(name, user, email, passw, passwVeri)
        if name == "" or user == "" or email == "" or passw == "" or passwVeri == "":
            tkinter.messagebox.showerror("Error", "All Fields Are Required", parent = self.account_tabview.tab("Register"))
        elif passw != passwVeri():
            tkinter.messagebox.showerror("Error" , "Passwords do not match", parent = self.account_tabview.tab("Register"))
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Delta321", database="tiptops")
                cur = con.cursor()
                cur.execute("select * from Accounts where username=%s", user)
                row = cur.fetchone()
                if row != None:
                    tkinter.messagebox.showerror("Error", "User Name Already Exist")
                else:
                    cur.execute("insert into Accounts(name, user, passw, email) values(%s,%s,%s,%s)",(name, user, passw, email))
                    con.commit() 
                    con.close()
                    tkinter.messagebox.showinfo("Success", "Registration Successful", parent = self.account_tabview.tab("Register"))
                    clear()
            except Exception as es:
                tkinter.messagebox.showerror("Error", f"Error Due to : {str(es)}", parent = self.account_tabview.tab("Register"))

        def clear():
            name.delete()
            user.delete()
            passw.delete()
            passwVeri.delete()
            email.delete()
        
    def delete():
        print("apple")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def log_in(self,loginUser, loginPassw):
        print("apple")

if __name__ == "__main__":
    app = App()
    app.mainloop()
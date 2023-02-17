import tkinter
import tkinter.messagebox
import customtkinter
import pymysql
from bs4 import BeautifulSoup
import requests

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
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Options", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        #Pricing Tab
        store_var = customtkinter.StringVar(value = "Lake County")
        self.pricing_combobox = customtkinter.CTkComboBox( self.tabview.tab("Pricing"), width= 140, values = ["Lake County", "Lake Tax", "Lake Clerk"], command = lambda: self.pricing_aggregate(store_var), variable = store_var)
        self.pricing_combobox.grid( row = 0, column= 0 )
        self.pricing_combobox.set("Lake County")

        #Invoices Tab
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
        self.appearance_mode_optionemenu.set("Dark")
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
        name_entry = customtkinter.CTkEntry(self.account_tabview.tab("Register"), width=125, height= 25, corner_radius=10, placeholder_text="Name")
        name_entry.grid( padx=25, pady = 10, sticky = "nw")
        user_entry = customtkinter.CTkEntry(self.account_tabview.tab("Register"), width=125, height= 25, corner_radius=10, placeholder_text="User Name")
        user_entry.grid( padx=25, pady = 10, sticky = "nw")
        passw_entry = customtkinter.CTkEntry(self.account_tabview.tab("Register"), width=125, height= 25, corner_radius=10, placeholder_text="Password")
        passw_entry.grid( padx=25, pady = 10, sticky = "nw")
        passw_Veri_entry = customtkinter.CTkEntry(self.account_tabview.tab("Register"), width=125, height= 25, corner_radius=10, placeholder_text="Verify Password")
        passw_Veri_entry.grid( padx=25, pady = 10, sticky = "nw")
        email_entry = customtkinter.CTkEntry(self.account_tabview.tab("Register"), width=125, height= 25, corner_radius=10, placeholder_text="Email")
        email_entry.grid( padx=25, pady = 10, sticky = "nw")
        signUpBtn = customtkinter.CTkButton(self.account_tabview.tab("Register"),width=125,height=25,corner_radius=10, text="Sign Up", command = lambda: self.register(name_entry, user_entry, email_entry, passw_entry, passw_Veri_entry))        
        signUpBtn.grid(padx = 25, pady = 10, sticky = "nw")

        #Login Form
        self.login = customtkinter.CTkLabel(self.account_tabview.tab("Login"), text="Login", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login.grid( padx=25, pady = 10, sticky = "nw")
        login_user_entry = customtkinter.CTkEntry(self.account_tabview.tab("Login"), width=125, height= 25, corner_radius=10, placeholder_text="User")
        login_user_entry.grid( padx=25, pady = 10, sticky = "nw")
        login_passw_entry = customtkinter.CTkEntry(self.account_tabview.tab("Login"), width=125, height= 25, corner_radius=10, placeholder_text="User")
        login_passw_entry.grid( padx=25, pady = 10, sticky = "nw")
        loginBtn = customtkinter.CTkButton(self.account_tabview.tab("Login"), width=125, height= 25, corner_radius=10, text="Sign Up", command = lambda: self.log_in(login_user_entry, login_passw_entry)) 
        loginBtn.grid(padx = 25, pady = 10, sticky = "nw")

    def register(self, name_entry, user_entry, email_entry, passw_entry, passw_Veri_entry):
        name = name_entry.get()
        user = user_entry.get()
        email = email_entry.get()
        passw = passw_entry.get()
        passwVeri = passw_Veri_entry.get()
        if name == "" or user == "" or email == "" or passw == "" or passwVeri == "":
            tkinter.messagebox.showerror("Error", "All Fields Are Required", parent = self.account_tabview.tab("Register"))
        elif passw != passwVeri:
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

    def log_in(self, login_user_entry, login_passw_entry):
        name = login_user_entry.get()
        passw = login_passw_entry.get()
        if name == "" or passw == "":
            tkinter.messagebox.showerror("error", "All Fields Required", parent = self.account_tabview.tab("Register"))
        else:
            con = pymysql.connect(host = "localhost", user = "root", password = "Delta321", database = "tiptops")
            cur = con.cursor()
            cur.execute("")
        

    def pricing_aggregate(self, store_var):

        store = store_var.get()

        print(store)

        my_data= []

        if store == "Lake Tax":
            urls = [
                'https://www.sanmar.com/p/2716_CloverGrn?text=s608',
                'https://www.sanmar.com/p/648_AthlGold?text=s608es',
                'https://www.sanmar.com/p/751_UltramrnBl?text=tls608',
                'https://www.sanmar.com/p/1694_DeepBerry?text=l608',
                'https://www.sanmar.com/p/2383_RoyClsNvy?text=s508',
                'https://www.sanmar.com/p/5682_DkGreenNv?text=tls508',
                'https://www.sanmar.com/p/1441_UltramrnBl?text=l508',
                'https://www.sanmar.com/p/2949_Charcoal?text=sp14',
                'https://www.sanmar.com/p/5745_PetrolBlue?text=sp14long',
                'https://www.sanmar.com/p/7_LightBlue?text=sp24',
                'https://www.sanmar.com/p/5746_LightBlue?text=sp24long',
                'https://www.sanmar.com/p/3832_Royal?text=k510',
                'https://www.sanmar.com/p/5623_Navy?text=tlk510',
                'https://www.sanmar.com/p/1225_StrongBlue?text=k500',
                'https://www.sanmar.com/p/2274_Navy?text=tlk500',
                'https://www.sanmar.com/p/1407_DeepBerry?text=l500',
                'https://www.sanmar.com/p/112_CoolGrey?text=k500p',
                'https://www.sanmar.com/p/5736_Royal?text=tlk500p',
                'https://www.sanmar.com/p/1557_Burgundy?text=k500ls',
                'https://www.sanmar.com/p/5735_CoolGrey?text=tlk500ls',
                'https://www.sanmar.com/p/1362_Royal?text=l500ls',
                'https://www.sanmar.com/p/3859_TrueNavy?text=st650',
                'https://www.sanmar.com/p/5656_KellyGreen?text=tst650',
                'https://www.sanmar.com/p/5494_Maroon?text=st651',
                'https://www.sanmar.com/p/4042_Royal?text=cs410',
                'https://www.sanmar.com/p/5687_DarkNavy?text=tlcs410',
                'https://www.sanmar.com/p/4043_DarkNavy?text=cs411',
                'https://www.sanmar.com/p/9068_DarkNavy?text=cs420',
                'https://www.sanmar.com/p/5002_Tan?text=cs410ls',
                'https://www.sanmar.com/p/8581_Scarlet?text=nea201',
                'https://www.sanmar.com/p/4121_SnrklBlBk?text=j304',
                'https://www.sanmar.com/p/4122_BlkBlk?text=l304',
                'https://www.sanmar.com/p/1890_KhkTrBlk',
                'https://www.sanmar.com/p/2874_TrBlkGrey?text=tlj754',
                'https://www.sanmar.com/p/657_TNvGyHRf?text=j754r',
                'https://www.sanmar.com/p/5214_CharChar?text=ne1020'
            ]
            
            for url in urls:
                
                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")
                prices = soup.find(class_='price').get_text()
                price = prices[15:20]
                newprice = "=" + price + "+8"
                colors = soup.find_all('span', attrs={'class':'swatch-name'})
                swatches = [color.get_text() for color in colors]
                style = soup.find(class_= 'product-style-number').get_text()
                my_data.append({"Style": style, "Color": swatches,"Price": price, "Newprice": newprice})
                print (style + " retrieved" )

        elif store == "Lake Clerk":
            urls = [
                'https://www.sanmar.com/p/2716_CloverGrn?text=s608',
                'https://www.sanmar.com/p/648_AthlGold?text=s608es',
                'https://www.sanmar.com/p/751_UltramrnBl?text=tls608',
                'https://www.sanmar.com/p/1694_DeepBerry?text=l608',
                'https://www.sanmar.com/p/2383_RoyClsNvy?text=s508',
                'https://www.sanmar.com/p/5682_DkGreenNv?text=tls508',
                'https://www.sanmar.com/p/1441_UltramrnBl?text=l508',
                'https://www.sanmar.com/p/2949_Charcoal?text=sp14',
                'https://www.sanmar.com/p/5745_PetrolBlue?text=sp14long',
                'https://www.sanmar.com/p/7_LightBlue?text=sp24',
                'https://www.sanmar.com/p/5746_LightBlue?text=sp24long',
                'https://www.sanmar.com/p/3832_Royal?text=k510',
                'https://www.sanmar.com/p/5623_Navy?text=tlk510',
                'https://www.sanmar.com/p/1225_StrongBlue?text=k500',
                'https://www.sanmar.com/p/2274_Navy?text=tlk500',
                'https://www.sanmar.com/p/1407_DeepBerry?text=l500',
                'https://www.sanmar.com/p/112_CoolGrey?text=k500p',
                'https://www.sanmar.com/p/5736_Royal?text=tlk500p',
                'https://www.sanmar.com/p/1557_Burgundy?text=k500ls',
                'https://www.sanmar.com/p/5735_CoolGrey?text=tlk500ls',
                'https://www.sanmar.com/p/1362_Royal?text=l500ls',
                'https://www.sanmar.com/p/3859_TrueNavy?text=st650',
                'https://www.sanmar.com/p/5656_KellyGreen?text=tst650',
                'https://www.sanmar.com/p/5494_Maroon?text=st651',
                'https://www.sanmar.com/p/4042_Royal?text=cs410',
                'https://www.sanmar.com/p/5687_DarkNavy?text=tlcs410',
                'https://www.sanmar.com/p/4043_DarkNavy?text=cs411',
                'https://www.sanmar.com/p/9068_DarkNavy?text=cs420',
                'https://www.sanmar.com/p/5002_Tan?text=cs410ls',
                'https://www.sanmar.com/p/8581_Scarlet?text=nea201',
                'https://www.sanmar.com/p/4121_SnrklBlBk?text=j304',
                'https://www.sanmar.com/p/4122_BlkBlk?text=l304',
                'https://www.sanmar.com/p/1890_KhkTrBlk',
                'https://www.sanmar.com/p/2874_TrBlkGrey?text=tlj754',
                'https://www.sanmar.com/p/657_TNvGyHRf?text=j754r',
                'https://www.sanmar.com/p/5214_CharChar?text=ne1020'
                ]

            for url in urls:

                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")
                prices = soup.find(class_='price').get_text()
                price = prices[15:20]
                newprice = "=" + price + "+8"
                colors = soup.find_all('span', attrs={'class':'swatch-name'})
                swatches = [color.get_text() for color in colors]
                style = soup.find(class_= 'product-style-number').get_text()
                my_data.append({"Style": style, "Color": swatches,"Price": price, "Newprice": newprice})
                print (style + " retrieved" )
        
        elif store == "Lake County":
            urls = [
                'https://www.sanmar.com/p/2716_CloverGrn?text=s608',
                'https://www.sanmar.com/p/648_AthlGold?text=s608es',
                'https://www.sanmar.com/p/751_UltramrnBl?text=tls608',
                'https://www.sanmar.com/p/1694_DeepBerry?text=l608',
                'https://www.sanmar.com/p/2383_RoyClsNvy?text=s508',
                'https://www.sanmar.com/p/5682_DkGreenNv?text=tls508',
                'https://www.sanmar.com/p/1441_UltramrnBl?text=l508',
                'https://www.sanmar.com/p/2949_Charcoal?text=sp14',
                'https://www.sanmar.com/p/5745_PetrolBlue?text=sp14long',
                'https://www.sanmar.com/p/7_LightBlue?text=sp24',
                'https://www.sanmar.com/p/5746_LightBlue?text=sp24long',
                'https://www.sanmar.com/p/3832_Royal?text=k510',
                'https://www.sanmar.com/p/5623_Navy?text=tlk510',
                'https://www.sanmar.com/p/1225_StrongBlue?text=k500',
                'https://www.sanmar.com/p/2274_Navy?text=tlk500',
                'https://www.sanmar.com/p/1407_DeepBerry?text=l500',
                'https://www.sanmar.com/p/112_CoolGrey?text=k500p',
                'https://www.sanmar.com/p/5736_Royal?text=tlk500p',
                'https://www.sanmar.com/p/1557_Burgundy?text=k500ls',
                'https://www.sanmar.com/p/5735_CoolGrey?text=tlk500ls',
                'https://www.sanmar.com/p/1362_Royal?text=l500ls',
                'https://www.sanmar.com/p/3859_TrueNavy?text=st650',
                'https://www.sanmar.com/p/5656_KellyGreen?text=tst650',
                'https://www.sanmar.com/p/5494_Maroon?text=st651',
                'https://www.sanmar.com/p/4042_Royal?text=cs410',
                'https://www.sanmar.com/p/5687_DarkNavy?text=tlcs410',
                'https://www.sanmar.com/p/4043_DarkNavy?text=cs411',
                'https://www.sanmar.com/p/9068_DarkNavy?text=cs420',
                'https://www.sanmar.com/p/5002_Tan?text=cs410ls',
                'https://www.sanmar.com/p/8581_Scarlet?text=nea201',
                'https://www.sanmar.com/p/4121_SnrklBlBk?text=j304',
                'https://www.sanmar.com/p/4122_BlkBlk?text=l304',
                'https://www.sanmar.com/p/1890_KhkTrBlk',
                'https://www.sanmar.com/p/2874_TrBlkGrey?text=tlj754',
                'https://www.sanmar.com/p/657_TNvGyHRf?text=j754r',
                'https://www.sanmar.com/p/5214_CharChar?text=ne1020'
            ]

            my_data= []

            for url in urls:

                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")
                prices = soup.find(class_='price').get_text()
                price = prices[15:20]
                newprice = "=" + price + "+8"
                colors = soup.find_all('span', attrs={'class':'swatch-name'})
                swatches = [color.get_text() for color in colors]
                style = soup.find(class_= 'product-style-number').get_text()
                my_data.append({"Style": style, "Color": swatches,"Price": price, "Newprice": newprice})
                print (style + " retrieved" )

if __name__ == "__main__":
    app = App()
    app.mainloop()
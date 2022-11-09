#Importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

#criar uma janela

jan = Tk()
jan.title ("Hi! Garden - Faça seu login")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width="false", height="false")        #não responsivo
jan.attributes("-alpha", 0.96)
jan.iconbitmap(default="D:\Progamming\Python\Projeto sistema de login\Logo\iconpng.ico")


#Carregar imagens
Logo = PhotoImage(file="D:\Progamming\Python\Projeto sistema de login\Logo\Logo.png")

#WIDGTES

LeftFrame = Frame(jan, width=200, height=300, bg="SpringGreen4", relief="raise")         #Frame lado esquerdo
LeftFrame.pack(side=LEFT)                                                            

RightFrame = Frame(jan, width=395, height=300, bg="coral", relief="raise")           #frame lado direito
RightFrame.pack(side=RIGHT)

#adição de Logo

Logolabel = Label(LeftFrame, image=Logo, bg="SpringGreen4")
Logolabel.place(x=0, y=50)

#Entrada de dados

UserLabel = Label(RightFrame, text="Usuário:", font=("Century Gothic", 12), bg="coral", fg="grey10")
UserLabel.place(x=10, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=80, y=100)

PasswordLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 12), bg="coral", fg="grey10" )
PasswordLabel.place(x=10, y=140)

PasswordEntry = ttk.Entry(RightFrame, width=30, show="•")
PasswordEntry.place(x=80, y=140)

#logando no sistema 

def Login():

    Usuario = UserEntry.get()
    Pass = PasswordEntry.get()

    #comparar entrada com Database
    
    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE User = ? AND Pass = ?
    """, (Usuario, Pass))

    VerifyLogin = DataBaser.cursor.fetchone()
    
    try:
        if (Usuario in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login", message="Logado com Sucesso")          
    except:
        messagebox.showinfo(title="Erro", message="Confira seu Cadastro")

#Botões
LoginButton = ttk.Button(RightFrame, text="Login", width=20, command=Login)
LoginButton.place(x=105, y=190)

def Register():
    
    #removendo widgets de login
    
    LoginButton.place(x=10000)
    RegisterButton.place(x=10000)
    
    #inserindo widgets de cadastro
    
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 12), bg="coral", fg="grey10")
    NomeLabel.place(x=10, y=20)

    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=80, y=20)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 12), bg="coral", fg="grey10")
    EmailLabel.place(x=10, y=60)

    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=80, y=60)

    #conectando ao banco de dados

    def RegisterToDataBase():
        
        #entrada de dados

        Name = NomeEntry.get()
        Email = EmailEntry.get()
        Usuario = UserEntry.get()
        Pass = PasswordEntry.get()
    
        if (Name == "" or Email == "" or Usuario == "" or Pass == ""):
            messagebox.showerror(title="Erro de Registro", message="Preencha Todos os Campos")
        else:
                #inserindo dados no DataBaser
                
            DataBaser.cursor.execute("""
                INSERT INTO Users(Name, Email, User, Pass) VALUES(?, ?, ?, ?)
                """, (Name, Email, Usuario, Pass))
            
                #conectando e salvando
                
            DataBaser.conn.commit()

                #mensagem de registro
                
            messagebox.showinfo(title="Registrar Info", message="Conta criada com sucesso")

    Register = ttk.Button(RightFrame, text="Registrar", width=20, command=RegisterToDataBase)
    Register.place(x=105, y=190)

    def BackToLogin():

            #remove os widgets de cadastro

            NomeLabel.place(x=10000)
            NomeEntry.place(x=10000)
            EmailLabel.place(x=10000)
            EmailEntry.place(x=10000)
            Register.place(x=10000)
            Back.place(x=10000)

            #trazendo de volta botões de login

            LoginButton.place(x=105, y=190)
            RegisterButton.place(x=105, y=220)

    Back = ttk.Button(RightFrame, text="Voltar", width=20, command=BackToLogin)
    Back.place(x=105, y=220)

RegisterButton = ttk.Button(RightFrame, text="Registro", width=20, command=Register)
RegisterButton.place(x=105, y=220)



#Fecha o Loop da interface (Start no pragrama)
jan.mainloop()
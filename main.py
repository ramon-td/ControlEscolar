import tkinter as tk
from tkinter import messagebox, ttk
from controlObjetos import Usuarios

#=============================================SETUP INICIAL=============================================
main =tk.Tk()
main.title("Control Escolar")
main.config(width=900, height=400)
#========================================================================================================

#=========================================DEFINICIÓN DE PESTAÑAS=========================================
#--------------------------------------------------MAIN--------------------------------------------------
pestanas =ttk.Notebook(main)
pestanas.grid(row=0)
#--------------------------------------------------LOGIN-------------------------------------------------
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Sesión")
pestanas.tab(0, state="normal")

#- - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - -
username_label = tk.Label(pestana_login, text="Username: ")
username_entry = tk.Entry(pestana_login)
password_label = tk.Label(pestana_login, text="Password: ")
password_entry = tk.Entry(pestana_login, show="•")

#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -
login_button = tk.Button(pestana_login, text="Login", command=lambda:login())
login_button.configure(width=10)
#- - - - - - - - - - - - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - - - - - - - - - -
username_label.grid(column=1, row=1, padx=10, pady=15)
password_label.grid(column=1, row=2, padx=10, pady=15)
username_entry.grid(column=2, row=1, padx=10, pady=15)
password_entry.grid(column=2, row=2, padx=10, pady=15)
login_button.grid(column=1, columnspan=2, row=4, padx=10, pady=15)

#------------------------------------------------------USUARIOS ----------------------------------------------
pestana_usuarios = ttk.Frame(pestanas)
pestanas.add(pestana_usuarios, text="Usuarios")
pestanas.tab(1, state="normal")
#- - - - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - - - 
user_code_label = tk.Label(pestana_usuarios, text="Ingrese codigo de usuario: ")
user_id_label = tk.Label(pestana_usuarios, text="ID:")
user_nombre_label = tk.Label(pestana_usuarios, text="Nombre: ")
user_apellidoP_label = tk.Label(pestana_usuarios, text="Apellido Paterno: ")
user_apellidoM_label = tk.Label(pestana_usuarios, text="Apellido Materno: ")
user_email_label = tk.Label(pestana_usuarios, text="Email: ")
user_username_label = tk.Label(pestana_usuarios, text="Nombre de usuario: ")
user_password_label = tk.Label(pestana_usuarios, text="Password: ")
user_perfil_label = tk.Label(pestana_usuarios, text="Perfil: ")
user_code_entry = tk.Entry(pestana_usuarios)
user_id_entry = tk.Entry(pestana_usuarios, state="disabled")
user_nombre_entry = tk.Entry(pestana_usuarios, state="disabled")
user_apellidoP_entry = tk.Entry(pestana_usuarios, state="disabled")
user_apellidoM_entry = tk.Entry(pestana_usuarios, state="disabled")
user_email_entry = tk.Entry(pestana_usuarios, state="disabled")
user_username_entry = tk.Entry(pestana_usuarios, state="disabled")
user_password_entry = tk.Entry(pestana_usuarios, state="disabled", show="•")
user_perfil_selection = tk.StringVar(main)
user_perfil_options = ("Administrador", "Maestro", "Alumno")
user_perfil_optionMenu = tk.OptionMenu(pestana_usuarios, user_perfil_selection, *user_perfil_options)
user_perfil_optionMenu.configure(state="disabled")

#- - - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - - - 
user_buscar_btn = tk.Button(pestana_usuarios, text="Buscar")
user_buscar_btn.configure(width=10)
user_nuevo_btn = tk.Button(pestana_usuarios, text="Nuevo")
user_nuevo_btn.configure(width=10)
user_guardar_btn = tk.Button(pestana_usuarios, text="Guardar")
user_guardar_btn.configure(width=10, state="disabled")
user_cancelar_btn = tk.Button(pestana_usuarios, text="Cancelar")
user_cancelar_btn.configure(width=10, state="disabled")
user_editar_btn = tk.Button(pestana_usuarios, text="Editar")
user_editar_btn.configure(width=10, state="disabled")
user_baja_btn = tk.Button(pestana_usuarios, text="Baja")
user_baja_btn.configure(width=10, state="disabled")

#- - - - - - - - - - - - - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - - - - - - - - - - - 
user_code_label.grid(column=1, columnspan=2, row=0, padx=10, pady=10, sticky=tk.E)
user_id_label.grid(column=0, columnspan=1, row=1, padx=10, pady=10, sticky=tk.E)
user_nombre_label.grid(column=0, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
user_apellidoP_label.grid(column=0, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
user_apellidoM_label.grid(column=0, columnspan=1, row=4, padx=10, pady=10, sticky=tk.E)
user_email_label.grid(column=0, columnspan=1, row=5, padx=10, pady=10, sticky=tk.E)
user_username_label.grid(column=2, columnspan=2, row=1, padx=10, pady=10, sticky=tk.E)
user_password_label.grid(column=3, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
user_perfil_label.grid(column=3, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
user_code_entry.grid(column=3, columnspan=2, row=0, padx=10, pady=10, sticky=tk.W)
user_code_entry.configure(width=30)
user_id_entry.grid(column=1, columnspan=1, row=1, padx=10, pady=10, sticky=tk.W)
user_id_entry.configure(width=15)
user_nombre_entry.grid(column=1, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
user_nombre_entry.configure(width=30)
user_apellidoP_entry.grid(column=1, columnspan=2, row=3, padx=10, pady=10, sticky=tk.W)
user_apellidoP_entry.configure(width=30)
user_apellidoM_entry.grid(column=1, columnspan=2, row=4, padx=10, pady=10, sticky=tk.W)
user_apellidoM_entry.configure(width=30)
user_email_entry.grid(column=1, columnspan=2, row=5, padx=10, pady=10, sticky=tk.W)
user_email_entry.configure(width=30)
user_username_entry.grid(column=4, columnspan=2, row=1, padx=10, pady=10, sticky=tk.W)
user_username_entry.configure(width=30)
user_password_entry.grid(column=4, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
user_password_entry.configure(width=30)
user_perfil_optionMenu.grid(column=4, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
user_perfil_optionMenu.configure(width=8)
user_buscar_btn.grid(column=5, columnspan=1, row=0, padx=10, pady=10, sticky=tk.E)
user_nuevo_btn.grid(column=1, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
user_guardar_btn.grid(column=2, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
user_cancelar_btn.grid(column=3, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
user_editar_btn.grid(column=4, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
user_baja_btn.grid(column=5, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)

#-------------------------------------------------------ALUMNOS ----------------------------------------------------
pestana_alumnos = ttk.Frame(pestanas)
pestanas.add(pestana_alumnos, text="Alumnos")
pestanas.tab(2, state="disabled")
#-------------------------------------------------------MAESTROS ---------------------------------------------------
pestana_maestros = ttk.Frame(pestanas)
pestanas.add(pestana_maestros, text="Maestros")
pestanas.tab(3, state="disabled")
#-------------------------------------------------------MATERIAS ---------------------------------------------------
pestana_materias = ttk.Frame(pestanas)
pestanas.add(pestana_materias, text="Materias")
pestanas.tab(4, state="disabled")
#--------------------------------------------------------GRUPOS ----------------------------------------------------
pestana_grupos = ttk.Frame(pestanas)
pestanas.add(pestana_grupos, text="Grupos")
pestanas.tab(5, state="disabled")
#--------------------------------------------------------HORARIO ---------------------------------------------------
pestana_horario = ttk.Frame(pestanas)
pestanas.add(pestana_horario, text="Horario")
pestanas.tab(6, state="disabled")
#---------------------------------------------------------SALON ----------------------------------------------------
pestana_salon = ttk.Frame(pestanas)
pestanas.add(pestana_salon, text="Salón")
pestanas.tab(7, state="disabled")
#--------------------------------------------------------CARRERA ---------------------------------------------------
pestana_carrera = ttk.Frame(pestanas)
pestanas.add(pestana_carrera, text="Carrera")
pestanas.tab(8, state="disabled")
#-------------------------------------------------------PLANEACIÓN -------------------------------------------------
pestana_planeacion = ttk.Frame(pestanas)
pestanas.add(pestana_planeacion, text="Planeación")
pestanas.tab(9, state="disabled")
#==============================================================================================================
#=======================================================AJUSTES DE POSICION====================================
test_label = tk.Label(pestana_usuarios, text="")
test_label.grid(column=6, row=6, sticky=tk.NSEW)
test_label.configure(width=18)
pestana_usuarios.columnconfigure(0, weight=1)
pestana_usuarios.columnconfigure(6, weight=1)
pestana_login.columnconfigure(0, weight=1)
pestana_login.columnconfigure(3, weight=1)
pestana_login.rowconfigure(0, weight=1)
pestana_login.rowconfigure(5, weight=1)
#===============================================================================================================
#======================================================FUNCIONES================================================
#----------------------------------------------Funcionamiento general-------------------------------------------
def dormirPestanas(code): #Se introduce un binario que indica que pestañas dormir y cuáles mantener despiertas
    for x in range(0, len(code)):
        if code[x] == '0':
            pestanas.tab(x, state="disable")
        else:
            pestanas.tab(x, state="normal")
def validarCampoNoVacio(lista):
    for x in lista:
        if x.get() == "":
            messagebox.showerror(title="Campo vacío", message="El campo " + str(x) + " no puede estar vacío")
            return False
    return True



#-----------------------------------------------------Login----------------------------------------------------
def login():
    listaUsuarios = Usuarios()
    listaUsuarios = listaUsuarios.listarUsuarios()
    listaCampos = {username_entry, password_entry}
    if validarCampoNoVacio(listaCampos):
        for x in range(len(listaUsuarios)):
            if username_entry.get() == listaUsuarios[x].get("Username"):
                if password_entry.get() == listaUsuarios[x].get("Password"):
                    if listaUsuarios[x].get("Permisos") == 4:
                        dormirPestanas("1111111111")
                    elif listaUsuarios[x].get("Permisos") == 3:
                        dormirPestanas("1101000000")
                    elif listaUsuarios[x].get("Permisos") == 2:
                        dormirPestanas("1110000000")
                    messagebox.showinfo(title="Bienvenido!", message="Bienvenido " + username_entry.get() + "!")
                    pestanas.select(pestana_usuarios)
                    clearLogin()
                    return 0
                else:
                    messagebox.showerror(title="Credenciales erróneas", message="Ha introducido una contraseña inválida")
                    return 0
        messagebox.showerror(title="Credenciales erróneas", message="No se encontró el nombre de usuario")

def clearLogin():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
#===============================================================================================================

dormirPestanas("1000000000")
main.mainloop()
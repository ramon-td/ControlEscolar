import tkinter as tk
from tkinter import messagebox, ttk

#========================================SETUP INICIAL=======================================
main =tk.Tk()
main.title("Control Escolar")
main.config(width=700, height=400)
#============================================================================================

#===================================DEFINICIÓN DE PESTAÑAS===================================
#------------------------------------MAIN------------------------------------
pestanas =ttk.Notebook(main)
pestanas.grid(row=0)
#------------------------------------LOGIN------------------------------------
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Sesión")
pestanas.tab(0, state="normal")

#- - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - -
username_label = tk.Label(pestana_login, text="Username: ")
username_entry = tk.Entry(pestana_login)
password_label = tk.Label(pestana_login, text="Password: ")
password_entry = tk.Entry(pestana_login, show="•")

#- - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - -
login_button = tk.Button(pestana_login, text="Login")
login_button.configure(width=10)

#- - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - -
#- - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - -
username_label = tk.Label(pestana_login, text="Username: ")
username_entry = tk.Entry(pestana_login)
password_label = tk.Label(pestana_login, text="Password: ")
password_entry = tk.Entry(pestana_login, show="•")

#- - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - -
login_button = tk.Button(pestana_login, text="Login")
login_button.configure(width=10)

#- - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - -
username_label.grid(column=0, row=1, padx=30, pady=15)
password_label.grid(column=0, row=2, padx=30, pady=15)
username_entry.grid(column=1, row=1, padx=30, pady=15)
password_entry.grid(column=1, row=2, padx=30, pady=15)
login_button.grid(column=0, columnspan=2, row=3, padx=30, pady=15)

#------------------------------------USUARIOS ------------------------------------
pestana_usuarios = ttk.Frame(pestanas)
pestanas.add(pestana_usuarios, text="Usuarios")
pestanas.tab(1, state="normal")
#- - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - -
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

#- - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - -
user_buscar_btn = tk.Button(pestana_usuarios, text="Buscar")
user_buscar_btn.configure(width=10)
user_nuevo_btn = tk.Button(pestana_usuarios, text="Nuevo")
user_nuevo_btn.configure(width=10)
user_guardar_btn = tk.Button(pestana_usuarios, text="Guardar")
user_guardar_btn.configure(width=10)
user_cancelar_btn = tk.Button(pestana_usuarios, text="Cancelar")
user_cancelar_btn.configure(width=10)
user_editar_btn = tk.Button(pestana_usuarios, text="Editar")
user_editar_btn.configure(width=10)
user_baja_btn = tk.Button(pestana_usuarios, text="Baja")
user_baja_btn.configure(width=10)

#- - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - -
user_code_label.grid(column=2, row=0, padx=10, pady=10)
user_id_label.grid(column=0, row=1, padx=10, pady=10)
user_nombre_label.grid(column=0, row=2, padx=10, pady=10)
user_apellidoP_label.grid(column=0, row=3, padx=10, pady=10)
user_apellidoM_label.grid(column=0, row=4, padx=10, pady=10)
user_email_label.grid(column=0, row=5, padx=10, pady=10)
user_username_label.grid(column=3, row=1, padx=10, pady=10)
user_password_label.grid(column=3, row=2, padx=10, pady=10)
user_perfil_label.grid(column=3, row=3, padx=10, pady=10)
user_code_entry.grid(column=3, columnspan=2, row=0, padx=10, pady=10)
user_id_entry.grid(column=1, row=1, padx=10, pady=10)
user_nombre_entry.grid(column=1, columnspan=2, row=2, padx=10, pady=10)
user_apellidoP_entry.grid(column=1, columnspan=2, row=3, padx=10, pady=10)
user_apellidoM_entry.grid(column=1, columnspan=2, row=4, padx=10, pady=10)
user_email_entry.grid(column=1, columnspan=2, row=5, padx=10, pady=10)
user_username_entry.grid(column=4, columnspan=2, row=1, padx=10, pady=10)
user_password_entry.grid(column=4, columnspan=2, row=2, padx=10, pady=10)
user_perfil_optionMenu.grid(column=4, row=3, padx=10, pady=10)
user_buscar_btn.grid(column=5, row=0, padx=10, pady=10)
user_nuevo_btn.grid(column=1, row=6, padx=10, pady=10)
user_guardar_btn.grid(column=2, row=6, padx=10, pady=10)
user_guardar_btn.grid(column=3, row=6, padx=10, pady=10)
user_cancelar_btn.grid(column=4, row=6, padx=10, pady=10)
user_editar_btn.grid(column=5, row=6, padx=10, pady=10)
user_baja_btn.grid(column=6, row=6, padx=10, pady=10)

#------------------------------------ALUMNOS ------------------------------------
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Alumnos")
pestanas.tab(2, state="disabled")
#------------------------------------MAESTROS ------------------------------------
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Maestros")
pestanas.tab(3, state="disabled")
#------------------------------------MATERIAS ------------------------------------
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Materias")
pestanas.tab(4, state="disabled")
#------------------------------------GRUPOS ------------------------------------
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Grupos")
pestanas.tab(5, state="disabled")
#------------------------------------HORARIO ------------------------------------
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Horario")
pestanas.tab(6, state="disabled")
#------------------------------------SALON ------------------------------------
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Salón")
pestanas.tab(7, state="disabled")
#------------------------------------CARRERA ------------------------------------
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Carrera")
pestanas.tab(8, state="disabled")
#------------------------------------PLANEACIÓN ------------------------------------
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Planeación")
pestanas.tab(9, state="disabled")
#============================================================================================



main.mainloop()